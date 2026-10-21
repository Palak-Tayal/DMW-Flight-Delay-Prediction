
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Flight Delay Predictor",
    page_icon="✈️",
    layout="wide"
)

# Load trained model
MODEL_PATH = Path(__file__).parent / "flight_delay_model.pkl"
model = joblib.load(MODEL_PATH)

# Page heading
st.title("✈️ Flight Departure Delay Predictor")
st.write(
    "Estimate departure delays using flight schedule, "
    "route, airline, and weather information."
)
st.info("Academic demonstration using a model trained on synthetic flight data.")

st.divider()

st.header("Enter Flight Details")

with st.form("flight_prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Flight Information")

        airline = st.selectbox(
            "Airline",
            ["6E", "AI", "IX", "QP", "S5", "SG", "I5"]
        )

        origin = st.selectbox(
            "Origin Airport",
            ["DEL", "BOM", "BLR", "MAA", "HYD", "CCU"]
        )

        destination = st.selectbox(
            "Destination Airport",
            ["BOM", "DEL", "BLR", "MAA", "HYD", "CCU"]
        )

        departure_hour = st.slider(
            "Scheduled Departure Hour",
            min_value=0,
            max_value=23,
            value=10
        )

        departure_minute = st.selectbox(
            "Scheduled Departure Minute",
            list(range(0, 60, 5))
        )

        distance = st.number_input(
            "Flight Distance (km)",
            min_value=1,
            max_value=6000,
            value=1000
        )

        month = st.selectbox(
            "Month",
            list(range(1, 13))
        )

        day = st.slider(
            "Day of Month",
            min_value=1,
            max_value=31,
            value=15
        )

        day_of_week = st.selectbox(
            "Day of Week (1 = Monday, 7 = Sunday)",
            list(range(1, 8)),
            index=2
        )

    with col2:
        st.subheader("Weather Conditions")

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-20.0,
            max_value=60.0,
            value=28.0
        )

        humidity = st.slider(
            "Relative Humidity (%)",
            min_value=0,
            max_value=100,
            value=60
        )

        precipitation = st.number_input(
            "Precipitation (mm)",
            min_value=0.0,
            max_value=500.0,
            value=0.0
        )

        rain = st.selectbox("Rain", [0, 1])

        cloud_cover = st.slider(
            "Cloud Cover (%)",
            min_value=0,
            max_value=100,
            value=30
        )

        wind_speed = st.number_input(
            "Wind Speed (km/h)",
            min_value=0.0,
            max_value=200.0,
            value=10.0
        )

        wind_direction = st.slider(
            "Wind Direction (degrees)",
            min_value=0,
            max_value=360,
            value=180
        )

        pressure = st.number_input(
            "Mean Sea-Level Pressure (hPa)",
            min_value=800.0,
            max_value=1100.0,
            value=1013.0
        )

        weather_code = st.number_input(
            "Weather Code",
            min_value=0,
            max_value=100,
            value=0
        )

    submitted = st.form_submit_button(
        "Predict Departure Delay",
        use_container_width=True
    )

if submitted:
    if origin == destination:
        st.error("Origin and destination airports must be different.")
    else:
        st.warning(
            "The input form is ready. We will connect it to the trained "
            "model after verifying the feature mapping."
        )
