import shap
import streamlit as st
from src.model_loader import load_model
from src.data_loader import load_dataset
from src.config import TUNED_XGBOOST_MODEL

@st.cache_resource
def get_shap_values():

    model = load_model(TUNED_XGBOOST_MODEL)

    df = load_dataset()

    X = df.drop(columns=["Visibility (km)"])
    X = X.sample(300, random_state=42)

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    return X, shap_values

import pandas as pd
import numpy as np


def get_feature_importance():

    X, shap_values = get_shap_values()

    importance = np.abs(shap_values).mean(axis=0)

    feature_df = pd.DataFrame(
        {
            "Feature": X.columns,
            "Importance": importance
        }
    )

    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=False
    )

    return feature_df