# Incident Recovery Assessment Application

This project is an incident recovery assessment application built using Streamlit. It aims to provide AI-powered predictions and recommendations for disaster recovery based on user inputs.

## Project Structure

```
incident-recovery-assessment
├── app.py                     # Main entry point for the Streamlit application
├── pages                      # Directory containing different pages of the app
│   └── 1_Predict.py          # Logic for predicting recovery times based on user inputs
├── models                     # Directory containing serialized models and encoders
│   ├── model.pkl             # Machine learning model for predicting recovery times
│   ├── country_encoder.pkl    # Encoder for transforming country names into numerical format
│   └── disaster_encoder.pkl    # Encoder for transforming disaster types into numerical format
├── requirements.txt           # Python dependencies required for the project
├── .streamlit                 # Configuration settings for the Streamlit application
│   └── config.toml           # Theme and layout preferences for the app
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd incident-recovery-assessment
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage Guidelines

- Upon running the application, users will be presented with a user-friendly interface to input incident details.
- The application will predict recovery times and provide recommendations based on the input data.
- Users can navigate through different sections of the application to view predictions, recommendations, and historical data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.