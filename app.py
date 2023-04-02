import streamlit as st
import pickle

pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)

st.title("Salary prediction")

a = float(st.number_input("Experience in years"))



btn = st.button("predict")

if btn:
    prediction=regressor.predict([[a]])
    st.text(prediction[0])