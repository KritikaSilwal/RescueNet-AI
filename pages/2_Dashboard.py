from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="RescueNet AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# RESCUENET AI - DASHBOARD THEME
# =========================================================

st.markdown("""
<style>

    /* =========================================
       GLOBAL BACKGROUND
       ========================================= */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 5%,
                rgba(37, 99, 235, 0.12),
                transparent 25%
            ),
            radial-gradient(
                circle at 10% 90%,
                rgba(245, 158, 11, 0.07),
                transparent 25%
            ),
            #0B1220 !important;

        color: #F8FAFC !important;
    }


    /* =========================================
       MAIN CONTENT
       ========================================= */

    .main {
        background-color: #0B1220 !important;
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }


    /* =========================================
       ALL HEADINGS
       ========================================= */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #F8FAFC !important;
    }


    /* =========================================
       NORMAL TEXT
       ========================================= */

    p,
    span,
    li,
    label,
    small {
        color: #E5E7EB !important;
    }


    /* Markdown text */
    [data-testid="stMarkdownContainer"] {
        color: #E5E7EB !important;
    }

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] li {
        color: #E5E7EB !important;
    }


    /* =========================================
       CAPTIONS / SECONDARY TEXT
       ========================================= */

    [data-testid="stCaptionContainer"] {
        color: #94A3B8 !important;
    }


    /* =========================================
       METRICS
       ========================================= */

    [data-testid="stMetric"] {
        background: #172235 !important;
        border: 1px solid #26364D !important;
        border-radius: 14px !important;
        padding: 1rem !important;
    }

    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-weight: 800 !important;
    }

    [data-testid="stMetricDelta"] {
        color: #CBD5E1 !important;
    }


    /* =========================================
       CARDS
       ========================================= */

    .rn-card {
        background: #172235 !important;
        border: 1px solid #2A3A52 !important;
        border-radius: 16px !important;
        padding: 1.2rem !important;
        color: #F8FAFC !important;
    }


    /* =========================================
       DATAFRAME / TABLE
       ========================================= */

    [data-testid="stDataFrame"] {
        border: 1px solid #2A3A52 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }

    [data-testid="stDataFrame"] * {
        color: #E5E7EB !important;
    }


    /* =========================================
       SELECTBOX
       ========================================= */

    .stSelectbox label {
        color: #E5E7EB !important;
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #172235 !important;
        border-color: #334155 !important;
        color: #F8FAFC !important;
    }

    .stSelectbox div[data-baseweb="select"] span {
        color: #F8FAFC !important;
    }


    /* =========================================
       NUMBER INPUT
       ========================================= */

    .stNumberInput label {
        color: #E5E7EB !important;
    }

    .stNumberInput input {
        background-color: #172235 !important;
        color: #F8FAFC !important;
        border-color: #334155 !important;
    }


    /* =========================================
       SLIDERS
       ========================================= */

    .stSlider label {
        color: #E5E7EB !important;
    }

    .stSlider [data-testid="stTickBarMin"],
    .stSlider [data-testid="stTickBarMax"] {
        color: #94A3B8 !important;
    }


    /* =========================================
       BUTTONS
       ========================================= */

    .stButton button {
        background-color: #172235 !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }

    .stButton button:hover {
        border-color: #F59E0B !important;
        color: #FFFFFF !important;
    }


    /* =========================================
       TABS
       ========================================= */

    .stTabs [data-baseweb="tab-list"] {
        background-color: #111A2B !important;
        border-radius: 10px !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: #94A3B8 !important;
    }

    .stTabs [aria-selected="true"] {
        color: #F8FAFC !important;
    }


    /* =========================================
       EXPANDERS
       ========================================= */

    [data-testid="stExpander"] {
        background-color: #172235 !important;
        border: 1px solid #2A3A52 !important;
        border-radius: 12px !important;
    }

    [data-testid="stExpander"] summary {
        color: #F8FAFC !important;
    }

    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span {
        color: #E5E7EB !important;
    }


    /* =========================================
       ALERT / INFO BOXES
       ========================================= */

    [data-testid="stAlert"] {
        color: #E5E7EB !important;
    }

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span {
        color: #E5E7EB !important;
    }


    /* =========================================
       SIDEBAR
       ========================================= */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #111827 0%,
                #0F172A 100%
            ) !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] a {
        color: #E5E7EB !important;
    }

    [data-testid="stSidebar"] [aria-current="page"] {
        color: #FFFFFF !important;
        background-color: #26354D !important;
    }


    /* =========================================
       HORIZONTAL RULES
       ========================================= */

    hr {
        border-color: #334155 !important;
    }


    /* =========================================
       LINKS
       ========================================= */

    a {
        color: #60A5FA !important;
    }

    a:hover {
        color: #F59E0B !important;
    }


    /* =========================================
       PLOTLY / CHART CONTAINER
       ========================================= */

    [data-testid="stPlotlyChart"] {
        background-color: #172235 !important;
        border: 1px solid #2A3A52 !important;
        border-radius: 14px !important;
        padding: 0.5rem !important;
    }


    /* =========================================
       CHECKBOX / RADIO
       ========================================= */

    .stCheckbox label,
    .stRadio label {
        color: #E5E7EB !important;
    }


    /* =========================================
       FILE UPLOADER
       ========================================= */

    [data-testid="stFileUploader"] {
        background-color: #172235 !important;
        border: 1px dashed #334155 !important;
        border-radius: 12px !important;
    }

    [data-testid="stFileUploader"] * {
        color: #E5E7EB !important;
    }

</style>
""", unsafe_allow_html=True)
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