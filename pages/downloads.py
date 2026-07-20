import streamlit as st
import pandas as pd

from components.theme import load_css
from src.model_metrics import get_model_metrics
from src.data_loader import load_dataset


def show():

    load_css("style.css")

    st.title(":material/download: Download Page")

    st.write(
        "Download prediction results, model metrics, and sample weather data."
    )

    st.divider()

    st.subheader("📄 Latest Prediction")

    if "prediction" in st.session_state:

        prediction_df = pd.DataFrame({
            "Predicted Visibility (km)": [st.session_state.prediction]
        })

        csv = prediction_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Prediction",
            data=csv,
            file_name="visibility_prediction.csv",
            mime="text/csv",
            use_container_width=True
        )

    else:

        st.info("Please make a prediction first.")

    st.divider()

    st.subheader("📊 Model Performance Metrics")

    metrics_df = get_model_metrics()

    csv = metrics_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Model Metrics",
        data=csv,
        file_name="model_performance_metrics.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    st.subheader("🌦️ Sample Weather Dataset")

    dataset = load_dataset()

    sample_csv = dataset.head(100).to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Sample Dataset",
        data=sample_csv,
        file_name="sample_weather_dataset.csv",
        mime="text/csv",
        use_container_width=True
    )