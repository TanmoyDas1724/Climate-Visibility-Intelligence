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

st.markdown("---")

st.subheader(":airplane: Features")

st.write(
    "Everything you need to analyze weather visibility using Artificial Intelligence."
)
col1, col2, col3, col4, col5 = st.columns(5)

# -------------------------
# Card 1
# -------------------------

with col1:
    st.info(":robot: AI Powered Models")

    st.write("""
Multiple ML models including

• Linear Regression

• Decision Tree

• Random Forest

• XGBoost
""")

# -------------------------
# Card 2
# -------------------------

with col2:
    st.info(":bar_chart: Explainable AI")

    st.write("""
Understand why every prediction
was made using SHAP Explainable AI.
""")

# -------------------------
# Card 3
# -------------------------

with col3:
    st.info(":chart_with_upwards_trend: Advanced Analytics")

    st.write("""
Interactive visualizations,
feature importance and
statistical insights.
""")

# -------------------------
# Card 4
# -------------------------

with col4:
    st.info(":material/download: Download Reports")

    st.write("""
Download prediction reports
in PDF and CSV format.
""")

with col5:
    st.info(":material/verified: Reliable & Fast")

    st.write("""
Optimized ML pipeline
with high accuracy and
fast predictions.
""")