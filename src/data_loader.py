import pandas as pd
import streamlit as st

from src.config import DATA_DIR


@st.cache_data
def load_dataset():
    """
    Load the processed dataset.
    """

    df = pd.read_csv(
        DATA_DIR / "processed" / "weather_feature_engineered.csv"
    )

    return df