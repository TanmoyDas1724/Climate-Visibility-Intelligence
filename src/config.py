from pathlib import Path

#Root Directory
BASE_DIR=Path(__file__).resolve().parent.parent

# Project Folder
DATA_DIR=BASE_DIR/"data"
MODEL_DIR=BASE_DIR/"models"
ASSETS_DIR=BASE_DIR/"assets"
LOG_DIR=BASE_DIR/"logs"

#Model files
LINEAR_MODEL=MODEL_DIR/"linear_regression_model.pkl"
DECISION_TREE=MODEL_DIR/"decision_tree_model.pkl"
RANDOM_FOREST_MODEL=MODEL_DIR/"random_forest_model.pkl"
XGBOOST_MODEL=MODEL_DIR/"xgboost_model.pkl"
TUNED_XGBOOST_MODEL=MODEL_DIR/"TUNED_XGBOOST_MODEL.PKL"