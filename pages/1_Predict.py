import streamlit as st
import pickle
import pandas as pd
# -----------------------------
# Load Model and Encoders
# -----------------------------

from pathlib import Path

@st.cache_resource
def load_resources():

    BASE_DIR = Path(__file__).resolve().parent.parent
    MODELS_DIR = BASE_DIR / "models"

    with open(MODELS_DIR / "model.pkl", "rb") as f:
        model = pickle.load(f)

    with open(MODELS_DIR / "country_encoder.pkl", "rb") as f:
        country_encoder = pickle.load(f)

    with open(MODELS_DIR / "disaster_encoder.pkl", "rb") as f:
        disaster_encoder = pickle.load(f)

    return model, country_encoder, disaster_encoder


model, country_encoder, disaster_encoder = load_resources()


st.set_page_config(page_title="Predict Incident", page_icon="🚨")

st.title("🚨 Incident Recovery Prediction")

st.markdown("### Enter Disaster Details")

country = st.selectbox(
    "Country",
    country_encoder.classes_
)
disaster = st.selectbox(
    "Disaster Type",
    disaster_encoder.classes_
)


severity = st.slider("Severity Index", 0.0, 10.0, 5.0)

casualties = st.number_input("Casualties", 0)

economic_loss = st.number_input("Economic Loss (USD)", 0.0)

response_time = st.number_input("Response Time (Hours)", 0.0)

aid_amount = st.number_input("Aid Amount (USD)", 0.0)
response_efficiency = st.slider(
    "Response Efficiency Score",
    0.0,
    100.0,
    50.0
)

latitude = st.number_input(
    "Latitude",
    value=0.0,
    format="%.6f"
)

longitude = st.number_input(
    "Longitude",
    value=0.0,
    format="%.6f"
)
year = st.number_input(
    "Year",
    min_value=2018,
    max_value=2035,
    value=2024
)

month = st.selectbox(
    "Month",
    list(range(1, 13))
)



 

if st.button("🚨 Predict Recovery"):

    # Encode categorical values
    country_encoded = country_encoder.transform([country])[0]
    disaster_encoded = disaster_encoder.transform([disaster])[0]

    # Create input dataframe
    input_data = pd.DataFrame({
    "country": [country_encoded],
    "disaster_type": [disaster_encoded],
    "severity_index": [severity],
    "casualties": [casualties],
    "economic_loss_usd": [economic_loss],
    "response_time_hours": [response_time],
    "aid_amount_usd": [aid_amount],
    "response_efficiency_score": [response_efficiency],
    "latitude": [latitude],
    "longitude": [longitude],
    "year": [year],
    "month": [month]
})

    # STEP 3: Make Prediction
    prediction = model.predict(input_data)[0]

    # STEP 4: Show Result
    st.success("Prediction Completed!")

    st.metric(
        "📅 Estimated Recovery Time",
        f"{prediction:.1f} Days"
    )