import pickle
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from utils.ui import inject_global_styles, render_footer, render_header, render_section_header, render_sidebar

st.set_page_config(page_title="Incident Recovery Assessment", page_icon="🚨", layout="wide")

# -----------------------------
# Paths / constants
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

FEATURES = [
    "country",
    "disaster_type",
    "severity_index",
    "casualties",
    "economic_loss_usd",
    "response_time_hours",
    "aid_amount_usd",
    "response_efficiency_score",
    "latitude",
    "longitude",
    "year",
    "month",
]

RISK_THRESHOLDS = {
    "low": 30,
    "medium": 60,
    "high": 90,
}

SYSTEM_NOTICE = (
    "This system is an AI-assisted decision-support prototype and should not replace "
    "trained emergency-management professionals or official emergency protocols."
)

# -----------------------------
# Resource loading
# -----------------------------
@st.cache_resource
def load_resources():
    with open(MODELS_DIR / "model.pkl", "rb") as f:
        model = pickle.load(f)
    with open(MODELS_DIR / "country_encoder.pkl", "rb") as f:
        country_encoder = pickle.load(f)
    with open(MODELS_DIR / "disaster_encoder.pkl", "rb") as f:
        disaster_encoder = pickle.load(f)
    return model, country_encoder, disaster_encoder


def safe_load_resources():
    try:
        return load_resources(), None
    except Exception as exc:
        return None, exc


# -----------------------------
# Logic helpers
# -----------------------------
def classify_risk(prediction_days: float) -> tuple[str, str]:
    if prediction_days < RISK_THRESHOLDS["low"]:
        return "Low", "🟢"
    if prediction_days < RISK_THRESHOLDS["medium"]:
        return "Medium", "🟡"
    if prediction_days < RISK_THRESHOLDS["high"]:
        return "High", "🟠"
    return "Critical", "🔴"


def operational_priority_score(
    severity: float,
    casualties: float,
    economic_loss: float,
    response_time: float,
    prediction_days: float,
) -> tuple[int, str]:
    severity_part = min((severity / 10.0) * 30.0, 30.0)
    casualties_part = min((casualties / 1000.0) * 20.0, 20.0)
    economic_part = min((economic_loss / 5_000_000.0) * 15.0, 15.0)
    response_part = min((response_time / 72.0) * 15.0, 15.0)
    recovery_part = min((prediction_days / 120.0) * 20.0, 20.0)

    score = round(severity_part + casualties_part + economic_part + response_part + recovery_part)
    score = max(0, min(100, score))

    if score >= 85:
        label = "Critical"
    elif score >= 65:
        label = "High"
    elif score >= 40:
        label = "Moderate"
    else:
        label = "Lower"

    return score, label


def build_recommendations(inputs: dict, prediction_days: float) -> list[str]:
    recs: list[str] = []

    if prediction_days >= 90:
        recs += [
            "Deploy additional rescue teams and activate extended recovery planning.",
            "Prepare temporary shelters and long-duration relief support.",
        ]
    elif prediction_days >= 60:
        recs += [
            "Increase medical coverage and sustain relief logistics.",
            "Coordinate additional field support for recovery operations.",
        ]

    if inputs["casualties"] >= 100:
        recs.append("Prioritize medical response and establish triage zones.")
    elif inputs["casualties"] >= 25:
        recs.append("Increase medical readiness and victim support capacity.")

    if inputs["severity_index"] >= 8:
        recs.append("Escalate the incident level and activate additional response units.")
    elif inputs["severity_index"] >= 6:
        recs.append("Maintain elevated monitoring and reinforce incident command.")

    if inputs["response_time_hours"] >= 24:
        recs.append("Improve rapid-response deployment and reassess team staging.")
    elif inputs["response_time_hours"] >= 12:
        recs.append("Reduce deployment delay and strengthen local response readiness.")

    if inputs["aid_amount_usd"] < inputs["economic_loss_usd"] * 0.1 and inputs["economic_loss_usd"] > 0:
        recs.append("Review resource allocation; current aid may be low relative to impact.")

    if inputs["response_efficiency_score"] < 50:
        recs.append("Improve coordination across rescue, logistics, and medical teams.")

    if inputs["disaster_type"].lower() in {"flood", "cyclone", "hurricane", "typhoon"}:
        recs.append("Prioritize sheltering, transport support, and water/sanitation resources.")

    if not recs:
        recs.append("Maintain monitoring and continue standard incident response planning.")

    return recs[:6]


def resource_advisor(severity: float, casualties: float, prediction_days: float) -> dict[str, str]:
    if severity >= 8 or casualties >= 100 or prediction_days >= 90:
        return {
            "Medical Teams": "Critical",
            "Rescue Teams": "Critical",
            "Shelters": "High",
            "Food & Water": "High",
            "Transport": "High",
            "Communication Units": "High",
        }
    if severity >= 6 or casualties >= 25 or prediction_days >= 60:
        return {
            "Medical Teams": "High",
            "Rescue Teams": "High",
            "Shelters": "Moderate",
            "Food & Water": "High",
            "Transport": "Moderate",
            "Communication Units": "Moderate",
        }
    return {
        "Medical Teams": "Moderate",
        "Rescue Teams": "Moderate",
        "Shelters": "Low",
        "Food & Water": "Moderate",
        "Transport": "Low",
        "Communication Units": "Low",
    }


def get_feature_importance(model):
    if not hasattr(model, "feature_importances_"):
        return None
    return pd.DataFrame(
        {"Feature": FEATURES, "Importance": model.feature_importances_}
    ).sort_values("Importance", ascending=False)


def predict_days(model, country_encoder, disaster_encoder, inputs: dict) -> float:
    country_encoded = country_encoder.transform([inputs["country"]])[0]
    disaster_encoded = disaster_encoder.transform([inputs["disaster_type"]])[0]

    input_data = pd.DataFrame(
        {
            "country": [country_encoded],
            "disaster_type": [disaster_encoded],
            "severity_index": [inputs["severity_index"]],
            "casualties": [inputs["casualties"]],
            "economic_loss_usd": [inputs["economic_loss_usd"]],
            "response_time_hours": [inputs["response_time_hours"]],
            "aid_amount_usd": [inputs["aid_amount_usd"]],
            "response_efficiency_score": [inputs["response_efficiency_score"]],
            "latitude": [inputs["latitude"]],
            "longitude": [inputs["longitude"]],
            "year": [inputs["year"]],
            "month": [inputs["month"]],
        }
    )

    return float(model.predict(input_data)[0])


def scenario_predict(model, country_encoder, disaster_encoder, base_inputs: dict, **overrides) -> float:
    scenario_inputs = base_inputs.copy()
    scenario_inputs.update(overrides)
    return predict_days(model, country_encoder, disaster_encoder, scenario_inputs)


def append_history(record: dict):
    if "incident_history" not in st.session_state:
        st.session_state.incident_history = []
    st.session_state.incident_history.insert(0, record)
    st.session_state.incident_history = st.session_state.incident_history[:25]


def build_briefing(inputs: dict, prediction: float, risk_label: str, priority_score: int, priority_label: str) -> str:
    return f"""INCIDENT SUMMARY
Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Country: {inputs["country"]}
Disaster: {inputs["disaster_type"]}
Severity: {inputs["severity_index"]:.1f}
Casualties: {int(inputs["casualties"])}
Economic Loss: ${inputs["economic_loss_usd"]:,.0f}
Response Time: {inputs["response_time_hours"]:.1f} hours
Aid Amount: ${inputs["aid_amount_usd"]:,.0f}
Efficiency: {inputs["response_efficiency_score"]:.1f}
Predicted Recovery: {prediction:.1f} days
Risk: {risk_label}
Operational Priority: {priority_score}/100 ({priority_label})
"""


# -----------------------------
# Styling
# -----------------------------
inject_global_styles()
render_sidebar()

st.markdown(
    """
    <style>
        .rn-hero-mini {
            background: linear-gradient(135deg, #0B1F3A 0%, #102A43 55%, #1D3557 100%);
            color: white;
            padding: 1.15rem 1.25rem;
            border-radius: 18px;
            box-shadow: 0 12px 30px rgba(11,31,58,0.12);
            margin-bottom: 1rem;
        }

        .rn-panel {
            background: #FFFFFF;
            border: 1px solid #D9E2EC;
            border-radius: 16px;
            padding: 1rem 1.05rem;
            box-shadow: 0 2px 10px rgba(11,31,58,0.04);
            margin-bottom: 1rem;
        }

        .rn-section-tag {
            display: inline-block;
            padding: 0.22rem 0.6rem;
            border-radius: 999px;
            background: #EAF2FF;
            color: #2563EB;
            font-size: 0.78rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }

        .rn-result {
            background: linear-gradient(135deg, #0B1F3A 0%, #132D4C 55%, #1D3557 100%);
            color: white;
            border-radius: 18px;
            padding: 1rem 1.05rem;
            box-shadow: 0 12px 30px rgba(11,31,58,0.12);
            border: 1px solid rgba(255,255,255,0.08);
        }

        .rn-result h2, .rn-result h3, .rn-result p { margin: 0; }

        .rn-pill {
            display: inline-block;
            padding: 0.22rem 0.65rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 850;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.14);
        }

        .rn-mini-card {
            background: #FFFFFF;
            border: 1px solid #D9E2EC;
            border-radius: 16px;
            padding: 0.9rem 0.95rem;
            box-shadow: 0 2px 10px rgba(11,31,58,0.04);
            height: 100%;
        }

        .rn-mini-title {
            color: #5E6C7B;
            font-size: 0.78rem;
            font-weight: 850;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 0.25rem;
        }

        .rn-mini-value {
            color: #0B1F3A;
            font-size: 1.05rem;
            font-weight: 850;
        }

        .rn-mini-note {
            color: #5E6C7B;
            margin-top: 0.25rem;
            font-size: 0.9rem;
        }

        .rn-radar {
            position: relative;
            overflow: hidden;
        }

        .rn-radar:after {
            content: "";
            position: absolute;
            right: -30px;
            top: -30px;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 1px solid rgba(255,255,255,0.10);
            box-shadow:
                0 0 0 20px rgba(255,255,255,0.03),
                0 0 0 45px rgba(255,255,255,0.02),
                0 0 0 70px rgba(255,255,255,0.015);
            opacity: 0.85;
            pointer-events: none;
        }

        .rn-reco-card {
            background: #FFFFFF;
            border: 1px solid #D9E2EC;
            border-radius: 16px;
            padding: 0.9rem 0.95rem;
            box-shadow: 0 2px 10px rgba(11,31,58,0.04);
            min-height: 120px;
        }

        .rn-progress-wrap {
            background: #EDF2F7;
            border-radius: 999px;
            overflow: hidden;
            height: 12px;
            border: 1px solid #D9E2EC;
        }

        .rn-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #2563EB 0%, #16A34A 100%);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="rn-hero-mini rn-radar">
        <div class="rn-pill">🟢 AI SYSTEM OPERATIONAL</div>
        <h1 style="margin:0.85rem 0 0 0;">🚨 INCIDENT RECOVERY ASSESSMENT</h1>
        <p style="margin:0.3rem 0 0 0; font-size:1rem;">AI-powered recovery prediction and emergency decision support.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption(SYSTEM_NOTICE)

resources, resource_error = safe_load_resources()
if resource_error:
    st.error("⚠️ Model resources could not be loaded.")
    st.exception(resource_error)
    st.stop()

model, country_encoder, disaster_encoder = resources

if "incident_history" not in st.session_state:
    st.session_state.incident_history = []

# -----------------------------
# Inputs
# -----------------------------
render_section_header("📍 Incident Information", "Core incident descriptors used by the model.")
a1, a2 = st.columns(2)
with a1:
    country = st.selectbox("Country", country_encoder.classes_, key="country")
    disaster = st.selectbox("Disaster Type", disaster_encoder.classes_, key="disaster")
with a2:
    year = st.number_input("Year", min_value=2018, max_value=2035, value=2024, step=1, key="year")
    month = st.selectbox("Month", list(range(1, 13)), key="month")

render_section_header("💥 Impact Assessment", "Severity and damage indicators.")
b1, b2, b3 = st.columns(3)
with b1:
    severity = st.slider("Severity Index", 0.0, 10.0, 5.0, key="severity")
with b2:
    casualties = st.number_input("Casualties", min_value=0, value=0, step=1, key="casualties")
with b3:
    economic_loss = st.number_input("Economic Loss (USD)", min_value=0.0, value=0.0, step=1000.0, key="economic_loss")

render_section_header("🚑 Response Capability", "Operational readiness indicators.")
c1, c2, c3 = st.columns(3)
with c1:
    response_time = st.number_input("Response Time (Hours)", min_value=0.0, value=0.0, step=1.0, key="response_time")
with c2:
    aid_amount = st.number_input("Aid Amount (USD)", min_value=0.0, value=0.0, step=1000.0, key="aid_amount")
with c3:
    response_efficiency = st.slider("Response Efficiency Score", 0.0, 100.0, 50.0, key="efficiency")

render_section_header("🌍 Location", "Geospatial inputs for mapping and analysis.")
d1, d2 = st.columns(2)
with d1:
    latitude = st.number_input("Latitude", value=0.0, format="%.6f", key="latitude")
with d2:
    longitude = st.number_input("Longitude", value=0.0, format="%.6f", key="longitude")

inputs = {
    "country": country,
    "disaster_type": disaster,
    "severity_index": float(severity),
    "casualties": float(casualties),
    "economic_loss_usd": float(economic_loss),
    "response_time_hours": float(response_time),
    "aid_amount_usd": float(aid_amount),
    "response_efficiency_score": float(response_efficiency),
    "latitude": float(latitude),
    "longitude": float(longitude),
    "year": int(year),
    "month": int(month),
}

st.markdown("---")
if st.button("🚨 PREDICT RECOVERY", use_container_width=True):
    try:
        prediction = predict_days(model, country_encoder, disaster_encoder, inputs)
        risk_label, risk_icon = classify_risk(prediction)
        priority_score, priority_label = operational_priority_score(
            severity, casualties, economic_loss, response_time, prediction
        )
        recommendations = build_recommendations(inputs, prediction)
        resources_df = resource_advisor(severity, casualties, prediction)
        importance_df = get_feature_importance(model)

        st.session_state.last_prediction = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **inputs,
            "prediction_days": prediction,
            "risk_label": risk_label,
            "priority_score": priority_score,
            "priority_label": priority_label,
        }
        append_history(st.session_state.last_prediction)

        # -----------------------------
        # Result dashboard
        # -----------------------------
        st.markdown(
            f"""
            <div class="rn-result">
                <div class="rn-pill">🟢 PREDICTION COMPLETED</div>
                <div style="margin-top:0.85rem;">
                    <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.06em; font-weight:800; opacity:0.9;">
                        Estimated Recovery
                    </div>
                    <div style="font-size:2.2rem; font-weight:900; line-height:1.1; margin-top:0.15rem;">
                        {prediction:.1f} DAYS
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        x1, x2, x3 = st.columns(3)
        with x1:
            st.markdown(
                f"""
                <div class="rn-mini-card">
                    <div class="rn-mini-title">Risk Level</div>
                    <div class="rn-mini-value">{risk_icon} {risk_label}</div>
                    <div class="rn-mini-note">Operational indicator</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with x2:
            st.markdown(
                f"""
                <div class="rn-mini-card">
                    <div class="rn-mini-title">Priority</div>
                    <div class="rn-mini-value">{priority_score}/100</div>
                    <div class="rn-mini-note">Response priority</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with x3:
            st.markdown(
                f"""
                <div class="rn-mini-card">
                    <div class="rn-mini-title">Priority State</div>
                    <div class="rn-mini-value">{priority_label}</div>
                    <div class="rn-mini-note">Operational classification</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("### 🧠 AI-Assisted Recommendations")
        reco_cols = st.columns(2)
        for idx, item in enumerate(recommendations):
            with reco_cols[idx % 2]:
                st.markdown(
                    f"""
                    <div class="rn-reco-card">
                        <div style="font-weight:850; color:#0B1F3A;">{['🚑 RESPONSE', '📦 RESOURCES', '🧭 COORDINATION', '🛟 LOGISTICS', '🏥 MEDICAL', '📡 COMMUNICATION'][idx]}</div>
                        <div class="rn-muted" style="margin-top:0.35rem;">{item}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown("### 📦 Resource Allocation Advisor")
        for item, level in resources_df.items():
            pct = {"Low": 0.30, "Moderate": 0.55, "High": 0.78, "Critical": 1.0}.get(level, 0.5)
            bar = int(pct * 10)
            st.markdown(
                f"""
                <div style="margin-bottom:0.65rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                        <b>{item}</b><span class="rn-muted">{level}</span>
                    </div>
                    <div class="rn-progress-wrap">
                        <div class="rn-progress-bar" style="width:{pct * 100:.0f}%;"></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("### 🔍 Why this prediction?")
        expl1, expl2, expl3 = st.columns(3)
        expl_rows = [
            ("Severity Index", f"{severity:.1f}", "Higher impact"),
            ("Casualties", f"{int(casualties)}", "Incident burden"),
            ("Response Time", f"{response_time:.1f} hours", "Operational delay"),
            ("Economic Loss", f"${economic_loss:,.0f}", "Higher impact"),
            ("Aid Amount", f"${aid_amount:,.0f}", "Response support"),
            ("Response Efficiency", f"{response_efficiency:.1f}", "Coordination quality"),
        ]
        for col, (label, value, note) in zip([expl1, expl2, expl3, expl1, expl2, expl3], expl_rows):
            with col:
                st.markdown(
                    f"""
                    <div class="rn-mini-card">
                        <div class="rn-mini-title">{label}</div>
                        <div class="rn-mini-value">{value}</div>
                        <div class="rn-mini-note">{note}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.info("These incident characteristics are associated with longer or shorter recovery periods in the trained model. This is model interpretation, not causation.")

        if importance_df is not None:
            st.markdown("### MODEL EXPLAINABILITY")
            st.markdown(
                """
                <div class="rn-panel">
                    Relative contribution of input features in the trained model.
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.bar_chart(importance_df.set_index("Feature"), width="stretch")

        st.markdown("### ⏱ Operational Planning Timeline")
        if prediction < 24:
            timeline = [
                "0–24 HOURS: Emergency Response",
                "24–72 HOURS: Stabilization",
                "3–14 DAYS: Relief Operations",
                "14+ DAYS: Recovery",
            ]
        elif prediction < 60:
            timeline = [
                "0–24 HOURS: Emergency Response",
                "24–72 HOURS: Stabilization",
                "3–14 DAYS: Relief Operations",
                "14+ DAYS: Recovery Planning",
            ]
        else:
            timeline = [
                "0–24 HOURS: Emergency Response",
                "24–72 HOURS: Stabilization",
                "3–14 DAYS: Prolonged Relief Operations",
                "14+ DAYS: Extended Recovery",
            ]

        tl_cols = st.columns(4)
        for col, step in zip(tl_cols, timeline):
            with col:
                st.markdown(
                    f"""
                    <div class="rn-mini-card">
                        <div class="rn-mini-title">Step</div>
                        <div class="rn-mini-value">{step.split(':')[0]}</div>
                        <div class="rn-mini-note">{step.split(':')[1].strip()}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        with st.expander("🔮 Response Scenario Simulator", expanded=True):
            st.markdown(
                """
                <div class="rn-panel">
                    <b>RESPONSE SCENARIO LAB</b><br>
                    Explore how changes in response conditions affect model-based recovery estimates.
                </div>
                """,
                unsafe_allow_html=True,
            )
            s1, s2 = st.columns(2)
            with s1:
                faster_response = st.number_input(
                    "Scenario A - Response Time (Hours)",
                    min_value=0.0,
                    value=max(0.0, response_time - 5.0),
                    step=1.0,
                    key="scenario_response_time",
                )
                higher_aid = st.number_input(
                    "Scenario B - Aid Amount (USD)",
                    min_value=0.0,
                    value=aid_amount + 100000.0,
                    step=1000.0,
                    key="scenario_aid",
                )
            with s2:
                higher_efficiency = st.slider(
                    "Scenario C - Response Efficiency",
                    0.0,
                    100.0,
                    min(100.0, response_efficiency + 20.0),
                    key="scenario_efficiency",
                )

            scenario_a = scenario_predict(
                model, country_encoder, disaster_encoder, inputs, response_time_hours=faster_response
            )
            scenario_b = scenario_predict(
                model, country_encoder, disaster_encoder, inputs, aid_amount_usd=higher_aid
            )
            scenario_c = scenario_predict(
                model, country_encoder, disaster_encoder, inputs, response_efficiency_score=higher_efficiency
            )

            scenario_df = pd.DataFrame(
                {
                    "Scenario": ["Current", "Faster Response", "Higher Aid", "Higher Efficiency"],
                    "Recovery Days": [
                        round(prediction, 1),
                        round(scenario_a, 1),
                        round(scenario_b, 1),
                        round(scenario_c, 1),
                    ],
                }
            )
            scenario_df["Change"] = ["Baseline"] + [
                f"↓ {prediction - val:.1f} days faster" for val in scenario_df["Recovery Days"].iloc[1:]
            ]
            st.dataframe(scenario_df, width="stretch", hide_index=True)

        with st.expander("📋 Incident Briefing", expanded=False):
            if "last_prediction" in st.session_state:
                report_text = build_briefing(
                    inputs,
                    prediction,
                    risk_label,
                    priority_score,
                    priority_label,
                )
                st.text_area("Briefing", report_text, height=260)
                st.download_button(
                    "⬇️ DOWNLOAD INCIDENT BRIEFING",
                    data=report_text,
                    file_name="rescuenet_incident_report.txt",
                    mime="text/plain",
                    use_container_width=True,
                )
            else:
                st.caption("Run a prediction first to generate a report.")

        with st.expander("🕘 Incident History", expanded=False):
            if st.session_state.incident_history:
                history_df = pd.DataFrame(st.session_state.incident_history)
                cols = [
                    "timestamp",
                    "country",
                    "disaster_type",
                    "severity_index",
                    "casualties",
                    "prediction_days",
                    "risk_label",
                    "priority_score",
                ]
                st.dataframe(history_df[cols], width="stretch", hide_index=True)
                if st.button("Clear Incident History", key="clear_history"):
                    st.session_state.incident_history = []
                    st.rerun()
            else:
                st.caption("No incidents recorded yet.")

        with st.expander("⚠️ Emergency Alert Panel", expanded=False):
            if prediction >= 90:
                st.error("🔴 CRITICAL INCIDENT: Recovery prediction exceeds 90 days.")
            elif prediction >= 60 or severity >= 8 or casualties >= 100:
                st.warning("🟠 HIGH PRIORITY: Severe incident with elevated casualties or prolonged recovery.")
            elif response_efficiency < 50 or response_time >= 24:
                st.warning("⚠️ RESOURCE WARNING: Response capacity may be insufficient.")
            else:
                st.success("🟢 No immediate alert escalation detected.")

    except Exception as exc:
        st.error("Prediction failed. Please review the selected inputs and try again.")
        st.exception(exc)

render_footer("RescueNet AI • AI-Powered Disaster Response & Recovery Decision Support • Hackathon Prototype")