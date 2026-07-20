import streamlit as st

from components.theme import load_css
from components.navbar import show_navbar
from components.footer import show_footer
from src.shap_utils import get_shap_values
from src.shap_utils import get_feature_importance
import shap
import matplotlib.pyplot as plt
import plotly.express as px


def show():

    load_css("style.css")

    show_navbar(
        "🧠 Explainability Dashboard",
        "Understand how the Tuned XGBoost model makes predictions using SHAP."
    )

    st.info(
        """
### What is SHAP?

SHAP (SHapley Additive exPlanations) explains how each feature
contributes to a machine learning prediction.

• Positive SHAP values increase the prediction.

• Negative SHAP values decrease the prediction.


"""
    )

    st.divider()

    st.subheader("📊 Global Feature Importance")

    X, shap_values = get_shap_values()

    fig, ax = plt.subplots(figsize=(10, 6))

    shap.summary_plot(
        shap_values,
        X,
        plot_type="bar",
        max_display=8,
        show=False
    )

    st.pyplot(fig)

    st.divider()

    st.subheader("📈 SHAP Summary Plot")

    fig, ax = plt.subplots(figsize=(10, 6))

    shap.summary_plot(
        shap_values,
        X,
        max_display=8,
        show=False
    )

    st.pyplot(fig)

    st.divider()

    feature_df = get_feature_importance()

    

    st.subheader("📊 Top 10 Feature Importance")

    fig = px.bar(
        feature_df.head(10),
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top 10 Important Features"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    show_footer()