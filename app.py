from datetime import datetime

import streamlit as st

from utils.ui import (
    inject_global_styles,
    render_footer,
    render_glass_card,
    render_hero,
    render_metric_card,
    render_section_header,
    render_sidebar,
)

st.set_page_config(
    page_title="RescueNet AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_global_styles()
render_sidebar()

if "incident_history" not in st.session_state:
    st.session_state.incident_history = []

last_prediction = st.session_state.get("last_prediction", {})
last_days = last_prediction.get("prediction_days")
last_risk = last_prediction.get("risk_label", "—")
last_priority = last_prediction.get("priority_score", "—")
last_timestamp = last_prediction.get(
    "timestamp",
    datetime.now().strftime("%Y-%m-%d %H:%M"),
)

left, right = st.columns([1.45, 1], gap="large")

with left:
    render_hero(
        status_text="AI SYSTEM OPERATIONAL",
        title="RESCUENET AI",
        subtitle="AI-Powered Disaster Response & Recovery Intelligence",
        tagline="Transforming disaster data into faster, smarter emergency decisions.",
    )

    c1, c2 = st.columns(2)
    with c1:
        st.page_link("pages/1_Predict.py", label="🚨 START INCIDENT ASSESSMENT →")
    with c2:
        st.page_link("pages/2_Dashboard.py", label="VIEW ANALYTICS →")

    st.markdown(
        """
        <div style="display:flex; gap:0.75rem; flex-wrap:wrap; margin-top:0.9rem;">
            <div class="rn-badge success"><span class="rn-status-dot green"></span>Prediction Engine Online</div>
            <div class="rn-badge info"><span class="rn-status-dot blue"></span>Historical Data Connected</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-info">
            <div class="rn-badge warn">
                <span class="rn-status-dot orange"></span>EMERGENCY INTELLIGENCE CONSOLE
            </div>
            <div class="rn-divider"></div>
            <div class="rn-mini-title">CURRENT INCIDENT</div>
        """,
        unsafe_allow_html=True,
    )

    if last_days is not None:
        render_metric_card(
            "Recovery Estimate",
            f"{float(last_days):.1f} DAYS",
            "Model-based estimate",
            "rn-topline-info",
        )
        render_metric_card(
            "Risk Level",
            str(last_risk),
            "Operational indicator",
            "rn-topline-warn",
        )
        render_metric_card(
            "Operational Priority",
            f"{last_priority} / 100",
            "Response priority score",
            "rn-topline-crit",
        )

        st.markdown(
            """
            <div class="rn-card rn-card-hover rn-topline-low" style="margin-top:1rem;">
                <div class="rn-mini-title">AI RECOMMENDATION</div>
                <div class="rn-mini-value" style="margin-top:0.25rem;">
                    Prioritize medical response and shelter coordination.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="rn-card rn-card-hover rn-topline-warn" style="margin-top:1rem;">
                <div class="rn-mini-title">CURRENT INCIDENT</div>
                <div class="rn-mini-value" style="margin-top:0.35rem;">
                    No prediction generated yet.
                </div>
                <div class="rn-mini-note">
                    Run an incident assessment to populate live intelligence.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<div class='rn-divider'></div>", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)
with k1:
    render_metric_card(
        "Session Incidents",
        str(len(st.session_state.incident_history)),
        "Predictions stored in this session",
        "rn-topline-info",
    )
with k2:
    render_metric_card(
        "Model Engine",
        "ONLINE",
        "Random Forest prediction service",
        "rn-topline-low",
    )
with k3:
    render_metric_card(
        "Decision Layer",
        "READY",
        "Risk, priority, and advisory logic active",
        "rn-topline-blue",
    )
with k4:
    render_metric_card(
        "Data Mode",
        "HISTORICAL",
        "Analysis only, not live authority data",
        "rn-topline-warn",
    )

l1, l2 = st.columns([1.2, 1], gap="large")

with l1:
    render_section_header("Mission Brief", "Command-center summary")
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-info">
            RescueNet AI supports emergency teams with recovery prediction,
            operational prioritization, explainable outputs, and response planning
            using the trained machine learning model.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_section_header("Current System Status")
    s1, s2, s3 = st.columns(3)
    s1.success("AI Engine Online")
    s2.success("Prediction Service Online")
    s3.success("Data Pipeline Online")

    render_section_header("What RescueNet AI Provides")
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-blue">
            <ul style="margin-bottom:0; color:#F8FAFC;">
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

with l2:
    render_section_header("Platform Modules")
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-info">
            <p style="margin:0 0 0.35rem 0;">
                <b>🚨 Incident Prediction</b><br>
                <span class="rn-muted">Enter disaster inputs and generate recovery estimates.</span>
            </p>
            <div class="rn-divider"></div>
            <p style="margin:0 0 0.35rem 0;">
                <b>📊 Analytics</b><br>
                <span class="rn-muted">Explore incident patterns and response trends.</span>
            </p>
            <div class="rn-divider"></div>
            <p style="margin:0 0 0.35rem 0;">
                <b>🌍 Disaster Map</b><br>
                <span class="rn-muted">Visualize incident locations and risk levels.</span>
            </p>
            <div class="rn-divider"></div>
            <p style="margin:0;">
                <b>ℹ️ About</b><br>
                <span class="rn-muted">Review model logic, scope, and limitations.</span>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_section_header("Quick Navigation")
    n1, n2 = st.columns(2)
    n1.page_link("pages/3_Map.py", label="🌍 Open Map")
    n2.page_link("pages/4_About.py", label="ℹ️ Open About")

    render_section_header("Deployment State")
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-low">
            <p style="margin:0 0 0.45rem 0;"><b>Model:</b> Random Forest Regressor</p>
            <p style="margin:0 0 0.45rem 0;"><b>Target:</b> Recovery Days</p>
            <p style="margin:0;"><b>Mode:</b> Historical decision support</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

render_footer(
    "RescueNet AI • AI-Powered Disaster Response & Recovery Decision Support • Prototype for Hackathon Demonstration"
)