import catboost as cb
import pandas as pd

from flask import Flask, jsonify, request

# Load the model
model = cb.CatBoostClassifier()
model.load_model("loan_dtm_model.cbm")

# Init the app
app = Flask("default")


# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    X = request.get_json()
    # Perform a prediction
    preds = model.predict(pd.DataFrame([X]))
    
    preds_list = preds.tolist()
    # Output json with prediction
    result = {"predictions":preds_list}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8888
    app.run(debug=True, host="0.0.0.0", port=8989)