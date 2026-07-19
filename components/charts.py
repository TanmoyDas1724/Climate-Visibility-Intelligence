import plotly.express as px
import streamlit as st


def bar_chart(df, x, y, title):

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def line_chart(df, x, y, title):

    fig = px.line(
        df,
        x=x,
        y=y,
        title=title,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def scatter_chart(df, x, y, color=None, title="Scatter Plot"):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title=title,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )



def correlation_heatmap(df):

    corr = df.select_dtypes(include="number").corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Correlation Heatmap"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )