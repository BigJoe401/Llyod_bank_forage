import joblib
import pandas as pd

model = joblib.load('models/cus_ch_pipeline.pkl')
threshold = joblib.load('models/threshold.pkl')
feature_names = joblib.load('models/feature_names.pkl')


def predict_churn(input_dict):
    df = pd.DataFrame([input_dict])

    # Ensure correct feature order
    df = df[feature_names]

    probability = model.predict_proba(df)[0, 1]
    prediction = int(probability >= threshold)

    return {
        'prediction': prediction,
        'probability': float(probability),
        'threshold': threshold,
        'label': 'Likely to Churn' if prediction == 1 else 'Likely to Stay'
    }