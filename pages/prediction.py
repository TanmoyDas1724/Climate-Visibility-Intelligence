import streamlit as st
from components.theme import load_css


def show():

    load_css("style.css")

    st.title(":crystal_ball: Prediction Page")