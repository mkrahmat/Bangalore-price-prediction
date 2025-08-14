# 🏠 Bangalore Price Prediction – Regression

A machine learning project to predict house prices in Bangalore using regression techniques.  
This project trains a model on real estate data, serves predictions via a Python Flask API, and provides a simple local web interface for interaction.

---

## 📌 Features
- **Data preprocessing & feature engineering** using Python and Pandas.
- **Model training** with regression algorithms (pickle format for deployment).
- **Flask server** to expose a REST API for predictions.
- **Local website** to input house details and get instant price predictions.
- End-to-end pipeline from `.ipynb` notebook → saved model → deployed web app.

---

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, scikit-learn, matplotlib)
- **Flask** (API backend)
- **HTML / CSS / JavaScript** (Frontend UI)
- **Jupyter Notebook** (Model building & experimentation)
- **Pickle** (Model serialization)

---

## 📂 Project Structure
├── client/ # Frontend code (HTML, CSS, JS)
├── server/ # Flask backend
├── model/ # Jupyter Notebook & pickle model files
├── .idea/ # IDE config (PyCharm)
└── README.md # Project documentation


---

## ⚙️ How It Works
1. **Data Preparation**: Clean and preprocess Bangalore housing dataset.
2. **Model Training**: Train a regression model to predict prices based on features like location, square footage, BHK, bathrooms, etc.
3. **Model Export**: Save the trained model as a `.pkl` file using `pickle`.
4. **API Creation**: Use Flask to serve the model and handle prediction requests.
5. **Frontend Integration**: Build a web form to send user inputs to the Flask API and display predictions.

---

## 🚀 Getting Started

```bash
### 1️⃣ Clone the repository
git clone https://github.com/mkrahmat/bangalore-price-prediction.git
cd bangalore-price-prediction

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the Flask server
cd server
python app.py

### 4️⃣ Open the local website

Visit:

http://127.0.0.1:5000/


Select house details → click Predict → see the predicted price.
