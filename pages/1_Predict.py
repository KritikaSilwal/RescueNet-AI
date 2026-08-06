import streamlit as st

st.set_page_config(page_title="Predict Incident", page_icon="🚨")

st.title("🚨 Incident Recovery Prediction")

st.markdown("### Enter Disaster Details")

country = st.text_input("Country")

disaster = st.selectbox(
    "Disaster Type",
    [
        "Earthquake",
        "Flood",
        "Hurricane",
        "Wildfire",
        "Tornado",
        "Extreme Heat",
        "Storm Surge",
        "Volcanic Eruption",
        "Landslide",
        "Drought"
    ]
)

severity = st.slider("Severity Index", 0.0, 10.0, 5.0)

casualties = st.number_input("Casualties", 0)

economic_loss = st.number_input("Economic Loss (USD)", 0.0)

response_time = st.number_input("Response Time (Hours)", 0.0)

aid_amount = st.number_input("Aid Amount (USD)", 0.0)

st.button("🚨 Predict Recovery")