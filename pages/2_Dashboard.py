from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="RescueNet AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Theme / styles
# -----------------------------
st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(29,53,87,0.08), transparent 28%),
                radial-gradient(circle at top right, rgba(214,40,40,0.06), transparent 22%),
                #F4F7FA;
        }

        .hero {
            background: linear-gradient(135deg, #081A2F 0%, #12304F 50%, #1D3557 100%);
            color: white;
            padding: 1.5rem 1.6rem;
            border-radius: 22px;
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 14px 36px rgba(11,31,58,0.18);
            margin-bottom: 1rem;
            position: relative;
            overflow: hidden;
        }

        .hero:after {
            content: "";
            position: absolute;
            right: -60px;
            top: -60px;
            width: 180px;
            height: 180px;
            background: rgba(255,255,255,0.08);
            border-radius: 50%;
        }

        .hero h1, .hero h2, .hero h3, .hero p {
            margin: 0;
            position: relative;
            z-index: 1;
        }

        .status-pill {
            display: inline-block;
            padding: 0.3rem 0.7rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.15);
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 0.02em;
        }

        .glass-card {
            background: rgba(255,255,255,0.9);
            border: 1px solid rgba(227,234,241,0.95);
            border-radius: 18px;
            padding: 1rem 1.1rem;
            box-shadow: 0 2px 10px rgba(11,31,58,0.04);
            backdrop-filter: blur(6px);
        }

        .metric-card {
            background: linear-gradient(180deg, #FFFFFF 0%, #FAFCFE 100%);
            border: 1px solid #E3EAF1;
            border-radius: 18px;
            padding: 1rem;
            min-height: 118px;
            box-shadow: 0 2px 10px rgba(11,31,58,0.04);
        }

        .metric-title {
            color: #5E6C7B;
            font-size: 0.8rem;
            font-weight: 800;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 0.25rem;
        }

        .metric-value {
            color: #0B1F3A;
            font-size: 1.75rem;
            font-weight: 850;
            line-height: 1.1;
        }

        .metric-note {
            color: #5E6C7B;
            font-size: 0.92rem;
            margin-top: 0.35rem;
        }

        .module-card {
            background: white;
            border: 1px solid #E3EAF1;
            border-radius: 18px;
            padding: 1rem 1.05rem;
            box-shadow: 0 2px 10px rgba(11,31,58,0.04);
        }

        .section-title {
            color: #0B1F3A;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin: 0.15rem 0 0.6rem 0;
        }

        .muted {
            color: #5E6C7B;
        }

        .divider-line {
            height: 1px;
            background: linear-gradient(90deg, transparent, #D9E2EC, transparent);
            margin: 1rem 0;
        }

        .footer {
            color: #5E6C7B;
            text-align: center;
            padding: 1rem 0 0.5rem 0;
            font-size: 0.9rem;
        }

        .badge {
            display: inline-block;
            padding: 0.22rem 0.65rem;
            border-radius: 999px;
            background: #E7F6EF;
            color: #2A9D8F;
            font-size: 0.8rem;
            font-weight: 800;
            border: 1px solid #CBEEDD;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session state
# -----------------------------
if "incident_history" not in st.session_state:
    st.session_state.incident_history = []

history_count = len(st.session_state.incident_history)
last_prediction = st.session_state.get("last_prediction", {})
last_days = last_prediction.get("prediction_days")
last_risk = last_prediction.get("risk_label", "—")
last_priority = last_prediction.get("priority_score", "—")
last_timestamp = last_prediction.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M"))

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.markdown("## 🚨 RESCUENET AI")
st.sidebar.caption("Emergency Operations & Decision Support")

st.sidebar.markdown("### Navigation")
st.sidebar.page_link("app.py", label="🏠 Command Center")
st.sidebar.page_link("pages/1_Predict.py", label="🚨 Incident Prediction")
st.sidebar.page_link("pages/2_Dashboard.py", label="📊 Analytics")
st.sidebar.page_link("pages/3_Map.py", label="🌍 Disaster Map")
st.sidebar.page_link("pages/4_About.py", label="🧠 About")

st.sidebar.markdown("---")
st.sidebar.markdown("### SYSTEM STATUS")
st.sidebar.markdown("🟢 **SYSTEM ONLINE**")
st.sidebar.write("Model: Random Forest")
st.sidebar.write("Prediction Engine: Operational")
st.sidebar.write("Mode: Historical decision support")

st.sidebar.markdown("---")
st.sidebar.info(
    "This system is an AI-assisted decision-support prototype and should not replace "
    "trained emergency-management professionals or official emergency protocols."
)

# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <div class="status-pill">🟢 COMMAND CENTER ONLINE</div>
        <h1 style="margin-top:0.85rem;">RescueNet AI</h1>
        <h3 style="margin-top:0.25rem; font-weight:500;">
            Disaster Response, Recovery Intelligence, and Operational Prioritization
        </h3>
        <p style="margin-top:0.7rem; font-size:1rem; max-width: 920px;">
            A command-style interface for incident prediction, analytics, mapping, and emergency planning.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Quick access
# -----------------------------
st.markdown("### Quick Access")
q1, q2, q3, q4 = st.columns(4)
with q1:
    st.page_link("pages/1_Predict.py", label="🚨 Predict")
with q2:
    st.page_link("pages/2_Dashboard.py", label="📊 Analytics")
with q3:
    st.page_link("pages/3_Map.py", label="🌍 Map")
with q4:
    st.page_link("pages/4_About.py", label="🧠 About")

st.markdown("---")

# -----------------------------
# Top metrics
# -----------------------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Session Incidents</div>
            <div class="metric-value">{history_count}</div>
            <div class="metric-note">Predictions stored in this session</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with m2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Model Engine</div>
            <div class="metric-value">Online</div>
            <div class="metric-note">Random Forest prediction service</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with m3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Decision Layer</div>
            <div class="metric-value">Ready</div>
            <div class="metric-note">Risk, priority, and recommendations active</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with m4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Data Mode</div>
            <div class="metric-value">Historical</div>
            <div class="metric-note">Analysis only, not live authority data</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### Command Center Overview")

# -----------------------------
# Main layout
# -----------------------------
left, right = st.columns([1.45, 1])

with left:
    st.markdown("#### Mission Brief")
    st.markdown(
        """
        <div class="glass-card">
            RescueNet AI supports emergency teams with recovery prediction, operational prioritization,
            explainable outputs, and response planning using the trained machine learning model.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Current Status")
    s1, s2, s3 = st.columns(3)
    s1.success("🟢 AI Engine Online")
    s2.success("🟢 Prediction Service Online")
    s3.success("🟢 Data Pipeline Online")

    st.markdown("#### Recent Incident Snapshot")
    if last_days is not None:
        a, b, c = st.columns(3)
        a.metric("Predicted Recovery", f"{float(last_days):.1f} days")
        b.metric("Risk Level", str(last_risk))
        c.metric("Priority", f"{last_priority}/100")
        st.caption(f"Last updated: {last_timestamp}")
    else:
        st.info("No prediction has been generated in this session yet.")

    st.markdown("#### What RescueNet AI Provides")
    st.markdown(
        """
        <div class="module-card">
            <ul style="margin-bottom:0;">
                <li>AI recovery-time prediction</li>
                <li>Recovery-based risk classification</li>
                <li>Operational priority scoring</li>
                <li>AI-assisted recommendations</li>
                <li>Scenario comparison and planning support</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Operational Snapshot")
    st.markdown(
        """
        <div class="glass-card">
            <b>Primary Focus:</b> Faster response planning<br>
            <b>Secondary Focus:</b> Prioritization and resource awareness<br>
            <b>Output Type:</b> Historical decision support
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown("#### Platform Modules")
    st.markdown(
        """
        <div class="module-card">
            <p><b>🚨 Incident Prediction</b><br><span class="muted">Enter disaster inputs and generate recovery estimates.</span></p>
            <div class="divider-line"></div>
            <p><b>📊 Analytics</b><br><span class="muted">Explore incident patterns and response trends.</span></p>
            <div class="divider-line"></div>
            <p><b>🌍 Disaster Map</b><br><span class="muted">Visualize incident locations and risk levels.</span></p>
            <div class="divider-line"></div>
            <p><b>🧠 About</b><br><span class="muted">Review model logic, scope, and limitations.</span></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Operational Note")
    st.warning(
        "This prototype provides AI-assisted decision support only and must not replace official emergency protocols."
    )

    st.markdown("#### Deployment State")
    st.markdown(
        """
        <div class="glass-card">
            <p style="margin:0 0 0.45rem 0;"><b>Model:</b> Random Forest Regressor</p>
            <p style="margin:0 0 0.45rem 0;"><b>Target:</b> Recovery Days</p>
            <p style="margin:0;"><b>Mode:</b> Historical decision support</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        RescueNet AI • AI-Powered Disaster Response & Recovery Decision Support • Hackathon Prototype
    </div>
    """,
    unsafe_allow_html=True,
)