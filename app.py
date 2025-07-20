from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form['age']),
        float(request.form['sex']),
        float(request.form['cp']),
        float(request.form['trestbps']),
        float(request.form['chol']),
        float(request.form['fbs']),
        float(request.form['restecg']),
        float(request.form['thalach']),
        float(request.form['exang']),
        float(request.form['oldpeak']),
        float(request.form['slope']),
        float(request.form['ca']),
        float(request.form['thal'])
    ]

    prediction = model.predict([np.array(features)])[0]

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
