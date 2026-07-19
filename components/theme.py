import streamlit as st
from pathlib import Path


def load_css(css_file_name):
    """
    Load CSS from app/styles folder.
    """

    css_path = (
        Path(__file__).parent.parent
        / "styles"
        / css_file_name
    )

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )