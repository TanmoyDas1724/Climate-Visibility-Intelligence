import streamlit as st


def metric_card(title, value, delta=None):
    st.metric(
        label=title,
        value=value,
        delta=delta,
    )


def info_card(title, content):
    st.info(title)
    st.write(content)


def success_card(message):
    st.success(message)


def warning_card(message):
    st.warning(message)


def error_card(message):
    st.error(message)