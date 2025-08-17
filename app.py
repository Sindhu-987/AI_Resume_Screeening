# app.py

from flask import Flask, request, render_template
import pickle
import os
from utils import clean_resume, label_encoder

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer
model_path = os.path.join("models", "random_forest_model.pkl")
encoder_path = os.path.join("models", "label_encoder.pkl")
vectorizer_path = os.path.join("models", "tfidf_vectorizer.pkl")  


model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))
label_encoder = pickle.load(open(encoder_path, "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        resume_text = request.form["resume"]
        cleaned_text = clean_resume(resume_text)
        vectorized = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized)
        try:
            predicted_category = label_encoder.inverse_transform(prediction)[0]
        except:
            predicted_category = prediction[0]

        return render_template("index.html", prediction_text=f"Predicted Job Category: {predicted_category}")

if __name__ == "__main__":
    app.run(debug=True)
