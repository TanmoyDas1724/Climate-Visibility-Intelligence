import streamlit as st

from components.theme import load_css
from components.footer import show_footer


def show():

    load_css("style.css")

    st.title(":material/info: About")

    st.write(
        "Learn more about the Climate Visibility Intelligence Dashboard."
    )

    st.divider()

    # -----------------------------------------------------
    # Project Overview
    # -----------------------------------------------------

    st.subheader("🌦️ Project Overview")

    st.write("""
The **Climate Visibility Intelligence Dashboard** is an end-to-end Machine Learning application
developed to predict atmospheric visibility using historical weather data.

The dashboard combines data analysis, machine learning, and explainable AI to help users
understand how different weather conditions influence visibility.
""")

    st.divider()

    # -----------------------------------------------------
    # Objectives
    # -----------------------------------------------------

    st.subheader("🎯 Project Objectives")

    st.markdown("""
- Predict atmospheric visibility using weather parameters.
- Compare multiple Machine Learning models.
- Explain model predictions using SHAP.
- Provide an interactive dashboard for data exploration.
""")

    st.divider()

    # -----------------------------------------------------
    # Technology Stack
    # -----------------------------------------------------

    st.subheader("🛠️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### Frontend
- Streamlit

### Backend
- Python
""")

    with col2:

        st.markdown("""
### Machine Learning
- Scikit-learn
- XGBoost

### Visualization
- Plotly
- Matplotlib
- SHAP
""")

    st.divider()

    # -----------------------------------------------------
    # Machine Learning Models
    # -----------------------------------------------------

    st.subheader("🤖 Machine Learning Models")

    st.markdown("""
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Baseline XGBoost
- ⭐ Tuned XGBoost (Best Performing Model)
""")

    st.divider()

    # -----------------------------------------------------
    # Dataset
    # -----------------------------------------------------

    st.subheader("📊 Dataset")

    st.markdown("""
**Dataset:** Weather History Dataset

**Target Variable**
- Visibility (km)

**Important Features**
- Temperature
- Apparent Temperature
- Humidity
- Wind Speed
- Wind Bearing
- Pressure
- Cloud Cover
- Weather Summary
- Season
""")

    st.divider()

    # -----------------------------------------------------
    # Future Improvements
    # -----------------------------------------------------

    st.subheader("🚀 Future Improvements")

    st.markdown("""
- Live Weather API integration
- Real-time visibility prediction
- Weather forecasting support
- Mobile responsive interface
- Cloud deployment
""")

    st.divider()

    # -----------------------------------------------------
    # Developer
    # -----------------------------------------------------

    st.subheader("👨‍💻 Developer")

    st.markdown("""
**Tanmoy Das**

**GitHub:** https://github.com/TanmoyDas1724

**LinkedIn:** https://www.linkedin.com/in/tanmoy-das-719379314/

""")

    show_footer()