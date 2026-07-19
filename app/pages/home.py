import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon=":house:",
    layout="wide"
)
with st.container():

    left_col, right_col = st.columns([2,1])

    with left_col:

        st.caption("🌤️ AI POWERED WEATHER INSIGHTS")

        st.title("Climate Visibility Intelligence Dashboard")

        st.write(
            """
            An advanced Machine Learning dashboard that predicts
            atmospheric visibility using real-time weather parameters.

            It also provides Explainable AI (SHAP),
            model comparison and interactive analytics.
            """
        )

        col1, col2 = st.columns(2)

        with col1:
            st.button("🚀 Make Prediction")

        with col2:
            st.button("📊 Explore Analytics")

    with right_col:

        st.image(
            "https://img.icons8.com/fluency/240/cloud.png",
            width=180
        )

        st.metric(
            label="Predicted Visibility",
            value="8.42 km",
            delta="Good Visibility"
        )