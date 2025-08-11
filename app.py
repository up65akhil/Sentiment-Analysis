from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import os

# Load model and vectorizer
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("sentiment.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        probability = np.max(model.predict_proba(X))

        label_map = {0: "Negative👎🏻😒😔", 1: "Positive👌🙂👍🏻❤️"}
        return jsonify({
            "prediction": label_map.get(prediction, str(prediction)),
            "probability": float(probability)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
