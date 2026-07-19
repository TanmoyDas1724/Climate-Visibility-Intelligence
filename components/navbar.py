import streamlit as st


def show_navbar(title: str, subtitle: str = ""):
    st.markdown(f"# {title}")

    if subtitle:
        st.caption(subtitle)

    st.divider()