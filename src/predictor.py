from src.model_loader import load_model
from src.preprocess import preprocess_input
from src.config import TUNED_XGBOOST_MODEL

def predict_visibility(use_input):
    model=load_model(TUNED_XGBOOST_MODEL)
    processed_data=preprocess_input(use_input)
    prediction=model.predict(processed_data)
    return prediction[0]