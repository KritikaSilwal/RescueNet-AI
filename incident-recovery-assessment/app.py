import streamlit as st

st.set_page_config(page_title="Incident Recovery Assessment", page_icon="🚨", layout="wide")

st.markdown(
    """
    <style>
        .hero {
            background: linear-gradient(90deg, #0B1F3A, #1D3557);
            color: white;
            padding: 1.2rem 1.4rem;
            border-radius: 16px;
            margin-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1 style="margin:0;">🚨 INCIDENT RECOVERY ASSESSMENT</h1>
      <p style="margin:0.35rem 0 0 0;">AI-powered recovery prediction and emergency decision support.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Navigation")
st.sidebar.markdown("[Predict Recovery](./pages/1_Predict.py)")

st.caption("This application provides AI-assisted predictions for incident recovery assessments.")