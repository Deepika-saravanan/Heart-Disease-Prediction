Heart Disease Prediction
A machine learning-based web application using Flask to predict the likelihood of heart disease based on user input.

🔍 Overview

This project applies a trained Random Forest Classifier to predict heart disease from user-submitted health metrics via a web interface.

---

📁 Project Structure

HEART_DISEASE_PREDICTION/
├── model/
│   └── heart_model.pkl         # Trained machine learning model
├── static/
│   └── style.css               # CSS for styling the UI
├── templates/
│   ├── index.html              # Input form for user data
│   └── result.html             # Displays prediction result
├── app.py                      # Main Flask application
├── heart.csv                   # Dataset used for training
├── model.pkl                   # (Legacy) model file
├── readme.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── train.py                    # Script to train the ML model

---

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/Deepika-saravanan/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction

2. Install Required Libraries

pip install -r requirements.txt

3. Run the Flask App

python app.py

The app will be accessible at http://127.0.0.1:5000/

---

💡 How it Works

- User enters health parameters in the form (age, cholesterol, etc.)
- Data is passed to the Flask backend
- Model makes a prediction using Random Forest Classifier
- Result is shown on a new page (positive/negative for heart disease)

---

🛠 Tech Stack

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- HTML, CSS

---

📂 Dataset

- Source: Kaggle - Heart Disease UCI Dataset
- File: `heart.csv`

---

✍️ Author

Deepika Saravanan
