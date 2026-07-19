import pandas as pd


def get_model_metrics():

    data = {
        "Model": [
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "Baseline XGBoost",
            "Tuned XGBoost"
        ],

        "MAE": [
            2.4960,
            1.5368,
            1.1873,
            1.4365,
            1.1977
        ],

        "RMSE": [
            3.0290,
            2.2878,
            1.8434,
            2.0404,
            1.7759
        ],

        "R² Score": [
            0.4813,
            0.7041,
            0.8079,
            0.7646,
            0.8217
        ]
    }

    return pd.DataFrame(data)