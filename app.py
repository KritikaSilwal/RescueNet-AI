import streamlit as st

st.set_page_config(
    page_title="RescueNet AI",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 RescueNet AI")

st.subheader("AI-Powered Disaster Response & Recovery Prediction")

st.write(
    """
Welcome to RescueNet AI.

This platform helps emergency management teams predict disaster recovery time and analyze disaster response.
"""
)
st.sidebar.title("🚨 RescueNet AI")

st.sidebar.success("Emergency Decision Support System")

st.sidebar.markdown("---")

st.sidebar.info("""
Built with

• Streamlit

• Machine Learning

• Python
""")
st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

h1{
    color:#D62828;
}

</style>
""", unsafe_allow_html=True)
st.title("🚨 RescueNet AI")

st.subheader("AI-Powered Disaster Response & Recovery Prediction")

st.markdown("""
### Welcome to RescueNet AI

RescueNet AI helps emergency response teams make faster and smarter decisions using Machine Learning.

### Key Features

- 🤖 Predict Disaster Recovery Time
- 📊 Disaster Analytics Dashboard
- 🌍 Interactive Disaster Map
- 💡 AI-Based Decision Support
""")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌍 Total Records", "50,000")

with col2:
    st.metric("🌪 Disaster Types", "10")

with col3:
    st.metric("🌎 Countries", "150+")

with col4:
    st.metric("🤖 ML Accuracy", "93.8%")

left, right = st.columns([2,1])

with left:

    st.markdown("## 📌 About RescueNet")

    st.write("""
RescueNet AI predicts disaster recovery time using Machine Learning.

It assists governments and disaster response organizations in planning rescue operations based on historical disaster data.
""")

with right:

    st.info("""
### Technologies

- Python
- Streamlit
- Gradient Boosting
- Pandas
- Scikit-Learn
- Plotly
""")