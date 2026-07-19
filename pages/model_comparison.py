import streamlit as st
import plotly.express as px

from components.theme import load_css
from components.navbar import show_navbar
from components.footer import show_footer

from src.model_metrics import get_model_metrics


def show():

    load_css("style.css")

    show_navbar(
        "📈 Model Comparison Dashboard",
        "Compare the performance of all trained machine learning models."
    )

    df = get_model_metrics()

    # --------------------------
    # Best Model
    # --------------------------

    best_model = df.loc[df["R² Score"].idxmax()]

    st.success(
        f"🏆 Best Model: {best_model['Model']} "
        f"(R² = {best_model['R² Score']:.4f})"
    )

    st.divider()

    # --------------------------
    # Comparison Table
    # --------------------------

    st.subheader("📋 Model Performance")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📊 R² Score Comparison")

    fig = px.bar(
        df,
        x="Model",
        y="R² Score",
        text="R² Score",
        title="Model Comparison by R² Score"
    )

    fig.update_traces(texttemplate="%{text:.4f}", textposition="outside")

    fig.update_layout(
        xaxis_title="Models",
        yaxis_title="R² Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    show_footer()