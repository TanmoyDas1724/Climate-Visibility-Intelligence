import joblib
import streamlit as st

@st.cache_resource
def load_model(model_path):
    # Load and cache a machine learning model.
    return joblib.load(model_path)