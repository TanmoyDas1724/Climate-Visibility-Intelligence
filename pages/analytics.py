import streamlit as st

from components.theme import load_css
from components.navbar import show_navbar
from components.footer import show_footer

from src.data_loader import load_dataset
import plotly.express as px
from components.charts import correlation_heatmap

def show():

    load_css("style.css")

    show_navbar(
        "📊 Analytics Dashboard",
        "Explore the weather dataset used to train the machine learning models."
    )
    df=load_dataset()

    # Dataset Summary

    st.subheader(":pushpin: Dataset Overview ")

    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Rows",df.shape[0])
    with col2:
        st.metric("Columns",df.shape[1])
    with col3:
        st.metric("Missing Values",df.isnull().sum().sum( ))
    with col4:
        st.metric("Duplicated Rows",df.duplicated().sum())
    st.divider()

    # Dataset Preview
    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

    st.divider()

    # Statistical Summary 

    st.subheader("📈 Statistical Summary")

    st.dataframe(df.describe())
    st.divider()

    st.subheader("📊 Feature Distribution")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    selected_feature = st.selectbox(
        "Select a Feature",
        numeric_columns
    )

    fig=px.histogram(
        df,x=selected_feature,
        nbins=40,
        title=f"{selected_feature} Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.subheader("📦 Box Plot")

    fig = px.box(
        df,
        y=selected_feature,
        title=f"{selected_feature} Box Plot"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("🔥 Correlation Heatmap")

    correlation_heatmap(df)

    show_footer()
    