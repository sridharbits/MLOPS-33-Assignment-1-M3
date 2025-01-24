from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd
import os

app = Flask(__name__)

os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/sridharbits/MLOPS-33-Assignment-1.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "sridharbits"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "0dbb82ae320f2c39dba3cb988fedd62d5c421ab0"

# Load the model from DagsHub
logged_model = 'runs:/03a61fb3169d43a186de63ae7c5ca6ed/model'
model = mlflow.pyfunc.load_model(logged_model)

# Define the column names based on your dataset
COLUMNS = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        input_data = request.get_json()
        # Convert JSON to DataFrame
        data = pd.DataFrame(input_data, columns=COLUMNS)
        # Make predictions
        predictions = model.predict(data)
        # Return predictions as JSON
        return jsonify(predictions.tolist())
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
