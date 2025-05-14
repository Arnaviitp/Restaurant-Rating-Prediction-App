# 🍽️ Restaurant Rating Prediction App

A machine learning-powered web application that predicts restaurant ratings based on features like location, cuisine, cost, and more.  
Built as a project by a Data Science student at IIT using **Python**, **scikit-learn**, and **Streamlit**.

🔗 **Live App**: [Click here to try it](https://restaurant-rating-prediction-app-havsyyu8hydddttujamutd.streamlit.app)

---

## 🚀 Features

- ✅ Predicts restaurant ratings using trained ML models
- ✅ User-friendly Streamlit interface
- ✅ Clean input form and live result display
- ✅ Real-world dataset from the food & hospitality industry
- ✅ Web deployed — no installation needed to try it out

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **ML Models:** Scikit-learn
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn

---

## 📂 Project Structure

```
restaurant-rating-prediction-app/
│
├── app.py                # Streamlit app file
├── model.pkl             # Trained machine learning model
├── preprocessing.py      # Feature encoding & transformation
├── requirements.txt      # List of Python dependencies
└── README.md             # Project documentation
```

---

## 📊 Input Features

The app takes the following inputs:

- Restaurant location
- Cuisine type
- Approximate cost for two
- Online ordering availability
- Table booking option
- Restaurant type
- Service type

These features are preprocessed and passed into the ML model for prediction.

---

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/restaurant-rating-prediction-app.git
   cd restaurant-rating-prediction-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📌 Future Enhancements

- Add support for multiple ML models and model selection
- Integrate live map or geolocation filtering
- Add visual explanation with SHAP or LIME for model interpretability

---

## 👤 Author

**Arnav Anand**  
📚 BSc (Hons) in Data Science and Applications, IIT  
🔗 [LinkedIn](https://www.linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
