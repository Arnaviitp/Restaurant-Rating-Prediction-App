import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

scaler = joblib.load("Scaler.pkl")

st.set_page_config(layout="wide")
st.title("Restaurant Rating Prediction App")

st.caption("This app helps you to predict a Resturant Review Class")

st.divider()

avragecost = st.number_input("Please Enter the Estimated avg cost for two", min_value=50,max_value=999999, value=1000, step=200)

tablebooking = st.selectbox("Resturant has Table Booking?" , ["Yes","No"])

onlinedelivery = st.selectbox("Resturant has online Booking?", ["Yes","No"])

pricerange = st.selectbox("What is Price Range (1 Cheapest, 4 Most Expensive)",[1,2,3,4])

pridictbutton = st.button("Predict the Review!")

st.divider()

model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0

deliverystatus = 1 if onlinedelivery == "Yes" else 0

values = [[avragecost,bookingstatus,deliverystatus,pricerange]]
my_X_values = np.array(values)

X = scaler.transform(my_X_values)

if pridictbutton:
    st.snow()

    prediction = model.predict(X)

    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")


