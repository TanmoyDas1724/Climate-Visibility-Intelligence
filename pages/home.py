import streamlit as st
from components.theme import load_css


def show():

    load_css("style.css")

    with st.container():

        left_col, right_col = st.columns([2, 1])

        with left_col:

            st.caption(":cloud: AI POWERED WEATHER INSIGHTS")

            st.title("Climate Visibility Intelligence Dashboard")

            st.write(
                """
                An advanced Machine Learning dashboard that predicts
                atmospheric visibility using real-time weather parameters.

                It also provides Explainable AI (SHAP), model comparison
                and interactive analytics.
                """
            )

            col1, col2 = st.columns(2)

            with col1:
                st.button(
                    ":rocket: Make Prediction",
                    use_container_width=True
                )

            with col2:
                st.button(
                    ":bar_chart: Explore Analytics",
                    use_container_width=True
                )

        with right_col:

            st.image(
                "https://cdn-icons-png.flaticon.com/512/1779/1779807.png",
                width=180
            )

            st.markdown("### Predicted Visibility")

            st.metric(
                label="",
                value="8.42 km",
                delta="Good Visibility"
            )

    st.divider()

    st.header(":airplane: Features")

    cols = st.columns(5)

    titles = [
        "AI Powered Models",
        "Explainable AI",
        "Advanced Analytics",
        "Download Reports",
        "Reliable & Fast"
    ]

    descriptions = [
        "Linear Regression\n\nDecision Tree\n\nRandom Forest\n\nXGBoost",
        "Understand every prediction using SHAP Explainable AI.",
        "Interactive charts and feature importance analysis.",
        "Export reports in PDF and CSV.",
        "Fast prediction pipeline using optimized ML models."
    ]

    for col, title, desc in zip(cols, titles, descriptions):

        with col:

            st.info(title)

            st.write(desc)