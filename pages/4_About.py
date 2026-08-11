import streamlit as st

from utils.ui import (
    inject_global_styles,
    render_footer,
    render_hero,
    render_section_header,
)

st.set_page_config(
    page_title="About | RescueNet AI",
    page_icon="🚨",
    layout="wide",
)

inject_global_styles()

# ---------------------------------------
# HERO
# ---------------------------------------

render_hero(
    status_text="AI SYSTEM OPERATIONAL",
    title="RESCUENET AI",
    subtitle="AI-Powered Disaster Response & Recovery Intelligence",
    tagline="Predict. Understand. Prioritize. Respond.",
)

# ---------------------------------------
# ABOUT
# ---------------------------------------

render_section_header("What is RescueNet AI?")

st.markdown(
    """
    <div class="rn-card rn-card-hover rn-topline-info">
        <p>
            RescueNet AI is an AI-assisted decision-support platform that helps
            emergency response teams estimate disaster recovery time, assess
            operational risk, prioritize response efforts, and explore
            disaster patterns using historical data and machine learning.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------
# THE CHALLENGE
# ---------------------------------------

render_section_header("🚨 The Challenge")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-crit">
            <h3>⏱️ Time Pressure</h3>
            <p>
                Emergency teams must make decisions quickly during crisis
                situations.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-warn">
            <h3>📦 Limited Resources</h3>
            <p>
                Medical teams, shelters, transport, and supplies may be limited.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="rn-card rn-card-hover rn-topline-info">
            <h3>📅 Recovery Uncertainty</h3>
            <p>
                Disaster recovery duration and response priorities can be
                difficult to estimate.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------
# OUR SOLUTION
# ---------------------------------------

render_section_header("💡 Our Solution")

st.markdown(
    """
    <div class="rn-card rn-card-hover rn-topline-low">
        <p>
            RescueNet AI combines historical disaster data, machine learning,
            risk classification, operational scoring, and geospatial
            visualization into one decision-support platform.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)

features = [
    ("🤖", "Recovery Prediction", "Estimate expected recovery duration."),
    ("⚠️", "Risk Assessment", "Identify operational risk levels."),
    ("📊", "Decision Support", "Generate priority and response insights."),
    ("🌍", "Disaster Mapping", "Visualize geographic incident patterns."),
]

for col, (icon, title, description) in zip(
    [c1, c2, c3, c4], features
):
    with col:
        st.markdown(
            f"""
            <div class="rn-card rn-card-hover">
                <h3>{icon} {title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------
# HOW IT WORKS
# ---------------------------------------

render_section_header("⚙️ How It Works")

steps = [
    ("01", "Incident Input", "Enter disaster and response information."),
    ("02", "Data Processing", "Inputs are encoded and prepared."),
    ("03", "ML Prediction", "Random Forest estimates recovery duration."),
    ("04", "Decision Layer", "Risk and operational priority are calculated."),
    ("05", "Visual Insights", "Results appear through analytics and maps."),
]

for number, title, description in steps:

    col1, col2 = st.columns([0.12, 0.88])

    with col1:
        st.markdown(
            f"### {number}"
        )

    with col2:
        st.markdown(
            f"**{title}**"
        )
        st.caption(description)

    st.divider()

# ---------------------------------------
# TECHNOLOGY
# ---------------------------------------

render_section_header("🛠 Technology")

tech = [
    "Python",
    "Streamlit",
    "Pandas",
    "Scikit-learn",
    "Random Forest",
    "Plotly",
    "Machine Learning",
]

st.markdown(
    " ".join(
        f'<span class="rn-badge info" style="margin:0.2rem;">{item}</span>'
        for item in tech
    ),
    unsafe_allow_html=True,
)

# ---------------------------------------
# RESPONSIBLE USE
# ---------------------------------------

render_section_header("⚠️ Responsible Use")

st.markdown(
    """
    <div class="rn-card rn-card-hover rn-topline-warn">
        <p>
            RescueNet AI is a prototype decision-support system based on
            historical data. It should support, not replace, trained
            emergency-management professionals, official emergency protocols,
            or real-time authoritative information.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------
# FOOTER
# ---------------------------------------

render_footer(
    "RescueNet AI • AI-Powered Disaster Response & Recovery Intelligence • Hackathon Prototype"
)