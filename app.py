
# IMPORTING DEPENDENCIES

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import numpy as np
import pickle

 # LOADING THE DATAS INTO THE check.pkl FILE
with open('check.pkl', "rb") as file:
    model = pickle.load(file)


# USING STREAMLIT CREATING UI FOR BACKGROUNDIMAGE

page_bg_img = '''
<style>
.stApp {
    background-image: url("https://res.cloudinary.com/dpkuxu8mr/image/upload/v1749922198/1304178_bypnwg.jpg");
    background-position:right;
    background-size: cover; 
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# USING STREAMLIT CREATING UI FOR BUTTON PROPERTIES

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #00CAFF;
        color: black;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)


#  TITLE OF THE WEB
st.title(":blue[Heart Disease Risk Prediction]")
st.write("Enter your health details to predict heart disease risk.")

# USER INPUTS
age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [1, 0])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol Level", min_value=100, max_value=400, value=200)
fbs = st.selectbox("Fasting Blood Sugar (1 = High, 0 = Normal)", [1, 0])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=220, value=150)
exang = st.selectbox("Exercise-Induced Angina (1 = Yes, 0 = No)", [1, 0])
oldpeak = st.number_input("ST Depression Induced", min_value=0.0, max_value=6.0, value=1.0)
slope = st.selectbox("Slope of ST Segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (0-3)", [0, 1, 2, 3])

# USER PREDICTION FUNCTION

user_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
if st.button("Predict"):
    prediction=model.predict(user_data)
    risk = (":red[THE PERSON HAS STROKE RISK]") if prediction[0] == 1 else (":green[THE PERSON DOES NOT HAVE STROKE RISK]")
    st.write(f"Predicted Heart Disease Risk: **{risk}**")





