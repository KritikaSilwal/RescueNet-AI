from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Disaster Map", page_icon="🌍", layout="wide")


st.markdown("""
<style>

    /* ==============================
       RESCUENET MAP - TEXT VISIBILITY
       ============================== */

    /* Main application background */
    .stApp {
        background-color: #0B1220 !important;
        color: #F8FAFC !important;
    }

    /* Main headings */
    h1, h2, h3, h4, h5, h6 {
        color: #F8FAFC !important;
    }

    /* Normal text */
    p, span, li, label {
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

    /* Captions / small secondary text */
    [data-testid="stCaptionContainer"] {
        color: #94A3B8 !important;
    }

    /* Selectbox labels */
    .stSelectbox label {
        color: #E5E7EB !important;
    }

    /* Slider labels */
    .stSlider label {
        color: #E5E7EB !important;
    }

    /* Number input labels */
    .stNumberInput label {
        color: #E5E7EB !important;
    }

    /* Metric labels */
    [data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
    }

    /* Metric values */
    [data-testid="stMetricValue"] {
        color: #F8FAFC !important;
    }

    /* Expander text */
    [data-testid="stExpander"] summary {
        color: #F8FAFC !important;
    }

    /* Expander content */
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span {
        color: #E5E7EB !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] a {
        color: #E5E7EB !important;
    }

    /* Sidebar selected item */
    [data-testid="stSidebar"] [aria-current="page"] {
        color: #FFFFFF !important;
    }

    /* Buttons */
    .stButton button {
        color: #F8FAFC !important;
    }

</style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <div class="hero">
        <h1 style="margin:0;">🌍 DISASTER MAP</h1>
        <p style="margin:0.35rem 0 0 0;">Incident locations, recovery risk, and geographic response awareness.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Historical map view only. Uses session predictions when available.")

history = st.session_state.get("incident_history", [])
df = pd.DataFrame(history)

sample_df = pd.DataFrame(
    [
        {
            "country": "Sample",
            "disaster_type": "Flood",
            "latitude": 23.0225,
            "longitude": 72.5714,
            "risk_label": "High",
            "prediction_days": 72.0,
            "priority_score": 74,
        },
        {
            "country": "Sample",
            "disaster_type": "Cyclone",
            "latitude": 19.0760,
            "longitude": 72.8777,
            "risk_label": "Critical",
            "prediction_days": 104.0,
            "priority_score": 89,
        },
    ]
)

if df.empty:
    st.info("No incident history found in this session. Showing sample locations.")
    map_df = sample_df.copy()
else:
    for col in [
        "latitude",
        "longitude",
        "risk_label",
        "prediction_days",
        "priority_score",
        "country",
        "disaster_type",
    ]:
        if col not in df.columns:
            df[col] = None

    map_df = df.dropna(subset=["latitude", "longitude"]).copy()

    if map_df.empty:
        st.warning("No usable latitude/longitude values found in session history. Showing sample locations.")
        map_df = sample_df.copy()

# Filters
st.markdown("### Map Filters")
c1, c2, c3 = st.columns(3)

with c1:
    country_options = ["All"] + sorted([str(x) for x in map_df["country"].fillna("Unknown").unique().tolist()])
    country_filter = st.selectbox("Country", country_options, key="map_country")

with c2:
    risk_options = ["All"] + sorted([str(x) for x in map_df["risk_label"].fillna("Unknown").unique().tolist()])
    risk_filter = st.selectbox("Risk Level", risk_options, key="map_risk")

with c3:
    numeric_days = pd.to_numeric(map_df["prediction_days"], errors="coerce").dropna()

    if numeric_days.empty:
        min_days, max_days = 0.0, 0.0
        day_range = (0.0, 0.0)
        st.caption("Recovery day filter unavailable for current data.")
    else:
        min_days = float(numeric_days.min())
        max_days = float(numeric_days.max())

        if min_days == max_days:
            day_range = (min_days, max_days)
            st.caption(f"Recovery days are constant at {min_days:.1f}; range filter disabled.")
        else:
            day_range = st.slider(
                "Recovery Days",
                min_value=min_days,
                max_value=max_days,
                value=(min_days, max_days),
                key="map_days",
            )

filtered = map_df.copy()
if country_filter != "All":
    filtered = filtered[filtered["country"].astype(str) == country_filter]
if risk_filter != "All":
    filtered = filtered[filtered["risk_label"].astype(str) == risk_filter]

filtered_days = pd.to_numeric(filtered["prediction_days"], errors="coerce")
filtered = filtered[(filtered_days >= day_range[0]) & (filtered_days <= day_range[1])]

# Summary cards
st.markdown("### Geographic Summary")
a, b, c, d = st.columns(4)
with a:
    st.metric("Mapped Incidents", len(filtered))
with b:
    st.metric("Countries", filtered["country"].nunique() if not filtered.empty else 0)
with c:
    st.metric(
        "Critical Cases",
        int((filtered["risk_label"].astype(str) == "Critical").sum()) if not filtered.empty else 0,
    )
with d:
    st.metric("Last Updated", datetime.now().strftime("%H:%M"))

st.markdown("### Incident Map")

map_points = filtered.copy()
map_points["latitude"] = pd.to_numeric(map_points["latitude"], errors="coerce")
map_points["longitude"] = pd.to_numeric(map_points["longitude"], errors="coerce")
map_points = map_points.dropna(subset=["latitude", "longitude"])

if map_points.empty:
    st.warning("No valid coordinates available after filtering.")
else:
    st.map(map_points[["latitude", "longitude"]], width="stretch")

st.markdown("### Incident Details")
show_cols = [
    "country",
    "disaster_type",
    "latitude",
    "longitude",
    "risk_label",
    "prediction_days",
    "priority_score",
]
st.dataframe(filtered[show_cols], width="stretch", hide_index=True)

st.markdown("### Map Notes")
st.markdown(
    """
    <div class="card">
        <span class="muted">
            This view supports operational awareness only. If coordinates are missing in the input data,
            the map will fall back to sample locations.
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("RescueNet AI • Disaster Map")