# AI-Powered Resume Screening & Job Role Prediction

An end-to-end Machine Learning + Deep Learning project that automates resume screening and predicts the most suitable job category based on the resume content. Built using Python, NLP, Scikit-learn, Deep Learning, and Flask.

## Project Overview

This project simulates a real-world HR tool that:
- Cleans and processes resumes
- Predicts the most relevant job role (e.g., Data Science, HR, Finance)
- Provides a web interface to paste resumes and get instant predictions

## Files Included

- `AI-Powered Resume Screening.ipynb` → Full training & evaluation notebook
- `app.py` → Flask backend for deployment
- `utils.py` → Preprocessing & helper functions
- `models/` → Trained `.pkl` files (Random Forest model, vectorizer, encoder)
- `templates/index.html` → UI for the Flask app
- `UpdatedResumeDataSet.csv` → Original Kaggle dataset
- `requirements.txt` → Required libraries
- `AI-Powered Resume Screening.pdf` → PDF version of full notebook

## Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- Deep Learning (Sequential + Dense Layers)
- Flask (for deployment)
- HTML (for UI)
- Jupyter Notebook

## 🚀 How to Run Locally

1. Clone the repo or download ZIP
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Flask app:
   ```bash
   python app.py
4. Open in browser:
   http://127.0.0.1:5000/

Model Pipeline

Step 1: Clean text (remove links, special characters, etc.)

Step 2: TF-IDF vectorization

Step 3: Train with Random Forest (or Deep Learning)

Step 4: Label encode the categories

Step 5: Predict from user input (resume)

Features

Predicts job category from raw resume text

Preprocessing and cleaning handled automatically

Built-in Flask web app

Accuracy > 98% with Random Forest & Deep Learning

Easy to customize or extend

Use Case

This project demonstrates real-world AI in HR automation and is perfect for showcasing:

NLP skills

Model deployment

Full ML pipeline

Web development with Flask


