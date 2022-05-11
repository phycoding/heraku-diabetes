import streamlit as st
import pandas as pd
from PIL import Image
import tensorflow as tf
dependencies = {
    ' binary_precision': 'https://raw.githubusercontent.com/streamlit/streamlit/master/examples/api_examples/keras_api/binary_precision.py',
}

@st.cache(allow_output_mutation=True)
def load(model_path):
    model = tf.keras.models.load_model(model_path,custom_objects=dependencies)
    return model

def inference(row, model, feat_cols):
    df = pd.DataFrame([row])
    X = df.values  
    features = pd.DataFrame(X, columns = feat_cols)
    element = (model.predict(df)*100).pop(0).pop(0)
    st.title("You are likely to have {} percent of diabetes".format(element))
        
    

st.title('Diabetes Prediction App')
st.write('The data for the following example is originally from the National Institute of Diabetes and Digestive and Kidney Diseases and contains information on females at least 21 years old of Pima Indian heritage.')
image = Image.open('diabetes.png')
st.image(image, use_column_width=True)
st.write('Please fill in the details of the person under consideration in the left sidebar and click on the button below!')

age =           st.sidebar.number_input("Age in Years", 1, 150, 25, 1)
pregnancies =   st.sidebar.number_input("Number of Pregnancies", 0, 20, 0, 1)
glucose =       st.sidebar.slider("Glucose Level", 0, 200, 25, 1)
skinthickness = st.sidebar.slider("Skin Thickness", 0, 99, 20, 1)
bloodpressure = st.sidebar.slider('Blood Pressure', 0, 122, 69, 1)
bmi =           st.sidebar.slider("BMI", 0.0, 67.1, 31.4, 0.1)
dpf =           st.sidebar.slider("Diabetics Pedigree Function", 0.000, 2.420, 0.471, 0.001)

row = [pregnancies, glucose, bloodpressure, skinthickness, bmi, dpf, age]

if (st.button('Find Health Status')):
    feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    model = load('my_model.h5')
    
    result = inference(row, model, feat_cols)
    st.title(result)
