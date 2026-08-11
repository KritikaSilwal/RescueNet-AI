import streamlit as st


def inject_global_styles():
    st.markdown(
        """
        <style>
            :root {
                --rn-bg: #0B1220;
                --rn-bg-2: #111827;
                --rn-card: rgba(24, 35, 53, 0.86);
                --rn-card-2: rgba(30, 42, 61, 0.92);
                --rn-text: #F8FAFC;
                --rn-text-2: #CBD5E1;
                --rn-muted: #94A3B8;
                --rn-border: rgba(255,255,255,0.08);
                --rn-orange: #F59E0B;
                --rn-orange-bright: #FFB000;
                --rn-red: #EF4444;
                --rn-green: #22C55E;
                --rn-blue: #3B82F6;
                --rn-shadow: 0 20px 50px rgba(0,0,0,0.35);
            }

            html, body, [class*="css"] {
                font-family: Inter, "Segoe UI", Roboto, sans-serif;
            }

            .stApp {
                background:
                    radial-gradient(circle at 75% 20%, rgba(245,158,11,0.10), transparent 30%),
                    radial-gradient(circle at 20% 80%, rgba(59,130,246,0.08), transparent 35%),
                    radial-gradient(circle at 50% 0%, rgba(255,255,255,0.04), transparent 20%),
                    linear-gradient(180deg, #0B1220 0%, #111827 100%);
                color: var(--rn-text);
            }

            .stApp::before {
                content: "";
                position: fixed;
                inset: 0;
                pointer-events: none;
                background-image:
                    linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
                background-size: 42px 42px;
                opacity: 0.15;
                z-index: 0;
            }

            .rn-shell {
                position: relative;
                z-index: 1;
            }

            .rn-hero {
                position: relative;
                overflow: hidden;
                background:
                    radial-gradient(circle at 78% 18%, rgba(245,158,11,0.12), transparent 22%),
                    radial-gradient(circle at 18% 82%, rgba(59,130,246,0.08), transparent 28%),
                    rgba(24, 35, 53, 0.86);
                border: 1px solid var(--rn-border);
                border-radius: 18px;
                box-shadow: var(--rn-shadow);
                padding: 1.35rem 1.45rem;
                margin-bottom: 1rem;
                backdrop-filter: blur(12px);
            }

            .rn-hero::after {
                content: "";
                position: absolute;
                right: -18px;
                top: -18px;
                width: 180px;
                height: 180px;
                border-radius: 50%;
                border: 1px solid rgba(255,255,255,0.08);
                box-shadow:
                    0 0 0 20px rgba(255,255,255,0.03),
                    0 0 0 45px rgba(255,255,255,0.02),
                    0 0 0 70px rgba(255,255,255,0.015);
                opacity: 0.9;
                pointer-events: none;
            }

            .rn-badge {
                display: inline-flex;
                align-items: center;
                gap: 0.4rem;
                padding: 0.28rem 0.72rem;
                border-radius: 999px;
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.02em;
                color: var(--rn-text);
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.10);
                backdrop-filter: blur(10px);
            }

            .rn-badge.success { box-shadow: 0 0 0 1px rgba(34,197,94,0.15) inset; }
            .rn-badge.warn { box-shadow: 0 0 0 1px rgba(245,158,11,0.15) inset; }
            .rn-badge.crit { box-shadow: 0 0 0 1px rgba(239,68,68,0.15) inset; }
            .rn-badge.info { box-shadow: 0 0 0 1px rgba(59,130,246,0.15) inset; }

            .rn-title {
                margin: 0.85rem 0 0 0;
                font-size: 2.35rem;
                line-height: 1.0;
                font-weight: 900;
                letter-spacing: -0.04em;
                color: var(--rn-text);
            }

            .rn-subtitle {
                margin: 0.28rem 0 0 0;
                font-size: 1.05rem;
                color: var(--rn-text-2);
                font-weight: 500;
            }

            .rn-tagline {
                margin: 0.7rem 0 0 0;
                color: var(--rn-orange-bright);
                font-weight: 700;
            }

            .rn-card,
            .rn-panel,
            .rn-metric,
            .rn-mini-card,
            .rn-reco-card,
            .rn-result-card,
            .rn-console,
            .rn-analysis-card {
                background: var(--rn-card);
                border: 1px solid var(--rn-border);
                border-radius: 16px;
                box-shadow: var(--rn-shadow);
                backdrop-filter: blur(12px);
                color: var(--rn-text);
            }

            .rn-card,
            .rn-panel {
                padding: 1rem 1.05rem;
            }

            .rn-card-hover:hover,
            .rn-metric:hover,
            .rn-mini-card:hover,
            .rn-reco-card:hover,
            .rn-console:hover,
            .rn-analysis-card:hover {
                transform: translateY(-2px);
                transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
                box-shadow: 0 24px 60px rgba(0,0,0,0.42);
                border-color: rgba(245,158,11,0.18);
            }

            .rn-section {
                color: var(--rn-text);
                font-weight: 850;
                margin: 0.2rem 0 0.5rem 0;
                letter-spacing: -0.02em;
            }

            .rn-muted { color: var(--rn-muted); }

            .rn-divider {
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.10), transparent);
                margin: 0.85rem 0;
            }

            .rn-footer {
                color: var(--rn-muted);
                text-align: center;
                font-size: 0.88rem;
                padding: 0.9rem 0 0.45rem 0;
            }

            .rn-topline-low { border-top: 4px solid var(--rn-green); }
            .rn-topline-info { border-top: 4px solid var(--rn-orange); }
            .rn-topline-warn { border-top: 4px solid var(--rn-orange-bright); }
            .rn-topline-crit { border-top: 4px solid var(--rn-red); }
            .rn-topline-blue { border-top: 4px solid var(--rn-blue); }

            .rn-metric {
                padding: 0.95rem 1rem;
                min-height: 110px;
            }

            .rn-label {
                color: var(--rn-muted);
                font-size: 0.75rem;
                font-weight: 850;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            .rn-value {
                color: var(--rn-text);
                font-size: 1.55rem;
                font-weight: 900;
                line-height: 1.1;
                margin-top: 0.2rem;
            }

            .rn-sub {
                color: var(--rn-text-2);
                font-size: 0.9rem;
                margin-top: 0.35rem;
            }

            .rn-pill {
                display: inline-flex;
                align-items: center;
                gap: 0.35rem;
                padding: 0.23rem 0.65rem;
                border-radius: 999px;
                font-size: 0.78rem;
                font-weight: 850;
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.10);
            }

            .rn-pill.success { color: var(--rn-green); }
            .rn-pill.warn { color: var(--rn-orange-bright); }
            .rn-pill.crit { color: var(--rn-red); }
            .rn-pill.info { color: var(--rn-blue); }

            .rn-progress-wrap {
                background: rgba(255,255,255,0.06);
                border-radius: 999px;
                overflow: hidden;
                height: 10px;
                border: 1px solid rgba(255,255,255,0.08);
            }

            .rn-progress-bar {
                height: 100%;
                background: linear-gradient(90deg, var(--rn-orange) 0%, var(--rn-orange-bright) 100%);
                box-shadow: 0 0 18px rgba(245,158,11,0.22);
            }

            .rn-mini-card {
                padding: 0.9rem 0.95rem;
                min-height: 112px;
            }

            .rn-mini-title {
                color: var(--rn-muted);
                font-size: 0.75rem;
                font-weight: 850;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.3rem;
            }

            .rn-mini-value {
                color: var(--rn-text);
                font-size: 1.06rem;
                font-weight: 850;
                line-height: 1.25;
            }

            .rn-mini-note {
                color: var(--rn-text-2);
                font-size: 0.9rem;
                margin-top: 0.3rem;
            }

            .rn-status-dot {
                display: inline-block;
                width: 9px;
                height: 9px;
                border-radius: 50%;
                margin-right: 0.45rem;
                box-shadow: 0 0 0 0 rgba(34,197,94,0.3);
                animation: rnPulse 2.2s infinite;
            }

            .rn-status-dot.green { background: var(--rn-green); }
            .rn-status-dot.orange { background: var(--rn-orange); }
            .rn-status-dot.red { background: var(--rn-red); }
            .rn-status-dot.blue { background: var(--rn-blue); }

            @keyframes rnPulse {
                0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.28); }
                70% { box-shadow: 0 0 0 8px rgba(34,197,94,0.00); }
                100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.00); }
            }

            /* Sidebar */
            div[data-testid="stSidebar"] {
                background:
                    radial-gradient(circle at top, rgba(245,158,11,0.08), transparent 28%),
                    linear-gradient(180deg, #0B1220 0%, #111827 100%);
                border-right: 1px solid rgba(255,255,255,0.08);
            }

            div[data-testid="stSidebar"] * {
                color: var(--rn-text) !important;
            }

            div[data-testid="stSidebar"] .stCaption,
            div[data-testid="stSidebar"] p,
            div[data-testid="stSidebar"] small {
                color: var(--rn-text-2) !important;
            }

            /* Buttons */
            .stButton button,
            button[kind="primary"] {
                border-radius: 12px !important;
                border: 1px solid rgba(245,158,11,0.30) !important;
                background: linear-gradient(135deg, var(--rn-orange) 0%, var(--rn-orange-bright) 100%) !important;
                color: #111827 !important;
                font-weight: 900 !important;
                box-shadow: 0 0 20px rgba(245,158,11,0.18) !important;
            }

            .stButton button:hover,
            button[kind="primary"]:hover {
                filter: brightness(1.05);
                transform: translateY(-1px);
                box-shadow: 0 0 26px rgba(245,158,11,0.25) !important;
            }

            .stDownloadButton button {
                border-radius: 12px !important;
                border: 1px solid rgba(255,255,255,0.12) !important;
                background: rgba(255,255,255,0.06) !important;
                color: var(--rn-text) !important;
                font-weight: 800 !important;
            }

            /* Inputs */
            .stTextInput input,
            .stNumberInput input,
            .stTextArea textarea,
            .stSelectbox div[data-baseweb="select"] > div,
            .stMultiSelect div[data-baseweb="select"] > div {
                background: #182335 !important;
                color: var(--rn-text) !important;
                border: 1px solid rgba(255,255,255,0.08) !important;
                border-radius: 12px !important;
            }

            .stSelectbox svg,
            .stMultiSelect svg {
                color: var(--rn-text-2) !important;
                fill: var(--rn-text-2) !important;
            }

            .stSlider [data-baseweb="slider"] > div > div {
                background: var(--rn-orange) !important;
            }

            /* Dataframes */
            .stDataFrame, .stTable {
                border-radius: 14px;
                overflow: hidden;
            }
            /* RESCUENET TEXT VISIBILITY FIX */

.stApp {
    color: #F8FAFC !important;
}

.stApp p {
    color: #CBD5E1 !important;
}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {
    color: #F8FAFC !important;
}

.stApp b,
.stApp strong {
    color: #F8FAFC !important;
}

/* Page links */
[data-testid="stPageLink"] a {
    color: #F8FAFC !important;
}

[data-testid="stPageLink"] a span {
    color: #F8FAFC !important;
}

[data-testid="stPageLink"] a:hover {
    color: #FBBF24 !important;
}

/* Buttons */
.stButton > button {
    color: #F8FAFC !important;
}

.stButton > button p,
.stButton > button span {
    color: #F8FAFC !important;
}

/* Labels */
.stApp label {
    color: #CBD5E1 !important;
}

/* Inputs */
.stApp input,
.stApp textarea {
    color: #F8FAFC !important;
}

/* Selectboxes */
[data-baseweb="select"] {
    color: #F8FAFC !important;
}

[data-baseweb="select"] * {
    color: #F8FAFC !important;
}

/* Metrics */
[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
}

[data-testid="stMetricValue"] {
    color: #F8FAFC !important;
}

/* Alerts */
[data-testid="stAlert"] p {
    color: #E2E8F0 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {
    color: #CBD5E1 !important;
}

/* Links */
.stApp a {
    color: #FBBF24 !important;
}
/* =========================================
   RESCUENET SIDEBAR
   ========================================= */

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: #0B1220 !important;
    color: #F8FAFC !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
}

/* Everything inside sidebar */
section[data-testid="stSidebar"] * {
    color: #CBD5E1 !important;
}

/* Sidebar navigation area */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
    background: #0B1220 !important;
}

/* Navigation links */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
    color: #CBD5E1 !important;
    background: transparent !important;
    border-radius: 10px !important;
    padding: 10px 12px !important;
    margin: 4px 8px !important;
    font-weight: 500 !important;
    text-decoration: none !important;
}

/* Navigation link text */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a span {
    color: #CBD5E1 !important;
}

/* Hover */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
    background: rgba(245, 158, 11, 0.12) !important;
}

section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover span {
    color: #FBBF24 !important;
}

/* Currently selected page */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(245, 158, 11, 0.15) !important;
    border-left: 3px solid #FBBF24 !important;
}

/* Selected page text */
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] span {
    color: #FBBF24 !important;
    font-weight: 700 !important;
}

/* Sidebar collapse button */
section[data-testid="stSidebar"] button {
    color: #F8FAFC !important;
}

section[data-testid="stSidebar"] button svg {
    color: #F8FAFC !important;
}

/* Sidebar markdown text */
section[data-testid="stSidebar"] .stMarkdown p {
    color: #CBD5E1 !important;
}

/* Sidebar headings */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4 {
    color: #F8FAFC !important;
}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_status_badge(text="AI SYSTEM OPERATIONAL", tone="success"):
    st.markdown(
        f"""
        <div class="rn-badge {tone}">
            <span class="rn-status-dot {'green' if tone == 'success' else 'orange' if tone == 'warn' else 'red' if tone == 'crit' else 'blue'}"></span>
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero(
    status_text="AI SYSTEM OPERATIONAL",
    title="RESCUENET AI",
    subtitle="AI-Powered Disaster Response & Recovery Intelligence",
    tagline='"Predict. Understand. Prioritize. Respond."',
):
    st.markdown(
        f"""
        <div class="rn-hero rn-card-hover">
            <div class="rn-badge success">
                <span class="rn-status-dot green"></span>{status_text}
            </div>
            <h1 class="rn-title">{title}</h1>
            <h3 class="rn-subtitle">{subtitle}</h3>
            <p class="rn-tagline">{tagline}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_header(
    status_text="AI SYSTEM OPERATIONAL",
    title="RESCUENET AI",
    subtitle="AI-Powered Disaster Response & Recovery Intelligence",
    tagline='"Predict. Understand. Prioritize. Respond."',
):
    render_hero(
        status_text=status_text,
        title=title,
        subtitle=subtitle,
        tagline=tagline,
    )


def render_sidebar():
    st.sidebar.markdown(
        """
        <div style="padding: 0.25rem 0 0.5rem 0;">
            <div style="font-size: 1.25rem; font-weight: 900; letter-spacing: -0.03em;">
                🚨 RESCUENET <span style="color:#F59E0B;">AI</span>
            </div>
            <div style="color:#CBD5E1; font-size:0.92rem; margin-top:0.2rem;">
                Emergency Intelligence Platform
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("### Navigation")
    st.sidebar.page_link("app.py", label="🏠 Command Center")
    st.sidebar.page_link("pages/1_Predict.py", label="🚨 Incident Prediction")
    st.sidebar.page_link("pages/2_Dashboard.py", label="📊 Analytics")
    st.sidebar.page_link("pages/3_Map.py", label="🌍 Disaster Map")
    st.sidebar.page_link("pages/4_About.py", label="ℹ️ About")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### SYSTEM STATUS")
    st.sidebar.markdown("🟢 AI Engine Online")
    st.sidebar.markdown("🟢 Prediction Service Online")
    st.sidebar.markdown("🟢 Data Pipeline Online")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### PROTOTYPE MODE")
    st.sidebar.caption("AI-assisted decision support.")
    st.sidebar.caption("Not a replacement for official emergency protocols.")


def render_metric_card(label, value, note="", top_class="rn-topline-info"):
    st.markdown(
        f"""
        <div class="rn-metric {top_class} rn-card-hover">
            <div class="rn-label">{label}</div>
            <div class="rn-value">{value}</div>
            <div class="rn-sub">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title, subtitle=""):
    st.markdown(f"### {title}")
    if subtitle:
        st.caption(subtitle)


def render_glass_card(title, body, accent="info", footer=""):
    accent_class = {
        "success": "rn-topline-low",
        "warn": "rn-topline-warn",
        "crit": "rn-topline-crit",
        "blue": "rn-topline-blue",
        "info": "rn-topline-info",
    }.get(accent, "rn-topline-info")

    st.markdown(
        f"""
        <div class="rn-card rn-card-hover {accent_class}">
            <div class="rn-mini-title">{title}</div>
            <div class="rn-mini-value">{body}</div>
            {"<div class='rn-mini-note'>" + footer + "</div>" if footer else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_risk_badge(risk_label):
    tone = {
        "Low": "success",
        "Medium": "warn",
        "High": "warn",
        "Critical": "crit",
    }.get(str(risk_label), "info")
    st.markdown(f'<span class="rn-pill {tone}">{risk_label}</span>', unsafe_allow_html=True)


def render_resource_bar(label, level, value=0.5):
    pct = max(0.0, min(1.0, float(value)))
    st.markdown(
        f"""
        <div style="margin-bottom: 0.75rem;">
            <div style="display:flex; justify-content:space-between; gap:1rem; margin-bottom:0.25rem;">
                <div style="font-weight:800; color:#F8FAFC;">{label}</div>
                <div style="color:#CBD5E1;">{level}</div>
            </div>
            <div class="rn-progress-wrap">
                <div class="rn-progress-bar" style="width:{pct * 100:.0f}%;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer(text="RescueNet AI • Modern Emergency Operations Center"):
    st.markdown("---")
    st.markdown(f'<div class="rn-footer">{text}</div>', unsafe_allow_html=True)