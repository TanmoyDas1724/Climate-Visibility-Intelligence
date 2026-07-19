import streamlit as st
from components.theme import load_css
from components.navbar import show_navbar
from components.footer import show_footer
from src.predictor import predict_visibility
from src.utils import get_season,is_weekend
from datetime import datetime


def show():

    load_css("style.css")

    show_navbar(
        "🔮 Visibility Prediction",
        "Predict atmospheric visibility using the trained Tuned XGBoost model."
    )

    left_col, right_col = st.columns([1.4, 1])

    # -----------------------------
    # Left Column
    # -----------------------------
    with left_col:

        st.subheader("🌦 Weather Parameters")

    with st.form("prediction_form"):

        st.markdown("### 🌡️ Temperature Information")

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=-50.0,
            max_value=60.0,
            value=20.0,
            step=0.1,
        )

        apparent_temperature = st.number_input(
            "Apparent Temperature (°C)",
            min_value=-50.0,
            max_value=60.0,
            value=20.0,
            step=0.1,
        )

        st.markdown("### 💧 Atmospheric Information")

        humidity = st.slider(
            "Humidity",
            0.0,
            1.0,
            0.50,
            0.01
        )

        loud_cover = st.slider(
            "Cloud Cover",
            0.0,
            1.0,
            0.50,
            0.01
        )

        pressure = st.number_input(
            "Pressure (millibars)",
            value=1015.0,
            step=0.1,
        )

        st.markdown("### 🌬️ Wind Information")

        wind_speed = st.number_input(
            "Wind Speed (km/h)",
            value=10.0,
            step=0.1,
        )

        wind_bearing = st.slider(
            "Wind Bearing (°)",
            0,
            360,
            180
        )

        st.markdown("### 📅 Date & Time")

        prediction_date = st.date_input("Date")

        prediction_time = st.time_input("Time")

        st.markdown("### ☁️ Weather Condition")

        summary = st.selectbox(
            "Weather Summary",
            [
                "Clear",
                "Partly Cloudy",
                "Mostly Cloudy",
                "Overcast",
                "Foggy",
                "Rain",
                "Light Rain",
                "Drizzle",
                "Windy"
            ]
        )

        precip_type = st.selectbox(
            "Precipitation Type",
            [
                "rain",
                "snow"
            ]
        )

        predict_button = st.form_submit_button(
            "🚀 Predict Visibility",
            use_container_width=True
        )

        if predict_button:
            dt=datetime.combine(prediction_date,prediction_time)
            month=dt.month
            season=get_season(month)
            user_input = {
                "Temperature (C)": temperature,
                "Apparent Temperature (C)": apparent_temperature,
                "Humidity": humidity,
                "Wind Speed (km/h)": wind_speed,
                "Wind Bearing (degrees)": wind_bearing,
                "Loud Cover": loud_cover,
                "Pressure (millibars)": pressure,

                "Year": dt.year,
                "Month": dt.month,
                "Day": dt.day,
                "Hour": dt.hour,
                "DayOfWeek": dt.weekday(),
                "IsWeekend": int(is_weekend(dt))
            }
            # Summary One-Hot Encoding
            summaries = [
                "Breezy",
                "Breezy and Dry",
                "Breezy and Foggy",
                "Breezy and Mostly Cloudy",
                "Breezy and Overcast",
                "Breezy and Partly Cloudy",
                "Clear",
                "Dangerously Windy and Partly Cloudy",
                "Drizzle",
                "Dry",
                "Dry and Mostly Cloudy",
                "Dry and Partly Cloudy",
                "Foggy",
                "Humid and Mostly Cloudy",
                "Humid and Overcast",
                "Humid and Partly Cloudy",
                "Light Rain",
                "Mostly Cloudy",
                "Overcast",
                "Partly Cloudy",
                "Rain",
                "Windy",
                "Windy and Dry",
                "Windy and Foggy",
                "Windy and Mostly Cloudy",
                "Windy and Overcast",
                "Windy and Partly Cloudy",
            ]

            for item in summaries:
                user_input[f"Summary_{item}"] = int(summary == item)

            user_input["Precip Type_rain"] = int(precip_type == "rain")
            user_input["Precip Type_snow"] = int(precip_type == "snow")

            for s in ["Autumn", "Spring", "Summer", "Winter"]:
                user_input[f"Season_{s}"] = int(season == s)

            prediction = predict_visibility(user_input)

            st.session_state.prediction = prediction



    # -----------------------------
    # Right Column
    # -----------------------------
    with right_col:

        st.subheader("📈 Prediction Result")

        if "prediction" not in st.session_state:
            st.session_state.prediction = None

        if st.session_state.prediction is None:

            st.info("Enter weather parameters and click **Predict Visibility**.")

        else:

            prediction = st.session_state.prediction

            st.metric(
                label="🌫️ Predicted Visibility",
                value=f"{prediction:.2f} km",
            )

            if prediction >= 10:
                st.success("🟢 Excellent Visibility")

            elif prediction >= 5:
                st.warning("🟡 Moderate Visibility")

            else:
                st.error("🔴 Poor Visibility")

            st.metric(
                "Model",
                "Tuned XGBoost"
            )

           

        show_footer()