import streamlit as st

st.set_page_config(
    page_title="Climate Visibility Intelligence",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.image(
        "https://img.icons8.com/fluency/96/cloud.png",
        width=80,
    )

    st.title("Climate Visibility")

    st.markdown("### Intelligence Dashboard")

    st.divider()

    st.info(
        """
        **Welcome!**

        This dashboard predicts visibility
        using Machine Learning and
        Explainable AI.
        """
    )

st.title("Climate Visibility Intelligence Dashboard")

st.subheader("AI Powered Weather Visibility Prediction")

st.write(
    """
    Welcome to the AI-powered Climate Visibility Intelligence Dashboard.

    This application predicts visibility using machine learning models,
    provides analytics, compares multiple models, and explains predictions using SHAP Explainable AI.
    """
)