import streamlit as st
import numpy as np
st.title("Symptoms checker")
st.sidebar.title("Select the symptoms you are facing")

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

model = load("soh.h5")




def inference(row, model, feat_cols):
    df = pd.DataFrame([row])
    X = df.values  
    features = pd.DataFrame(X, columns = feat_cols)
    element = model.predict(df)
    for i in element:
        for j in i:
            result = j
    if element <= 0.5:
        st.title("You are likely to have {} percent chance of diabetes".format(round(result*100,2)))
        st.write("You are a healthy person")
    else:
        st.title("You are likely to have {} percent of diabetes".format(round(result*100,2)))
        st.write("Be careful you are a diabetic person")

st.sidebar.title('Choose only 17 features')

st.button('Predict')
options = st.sidebar.multiselect(
    'What are your symptoms',
    ['fatigue', 'weight_loss', 'cough', 'vomiting','breathlessness','headache','chest_pain','muscle_weakness',
    'stiff_neck','skin_rash','joint_pain','restlessness','high_fever','sweating','dizziness','swelling_joints',
    'skin_peeling','lethargy','loss_of_balance','movement_stiffness','silver_like_dusting','irregular_sugar_level',
    'family_history','lack_of_concentration','painful_walking','small_dents_in_nails','blurred_and_distorted_vision',
    'mucoid_sputum','inflammatory_nails','obesity','excessive_hunger','increased_appetite','polyuria'])

st.write('You selected:', options)

if len(options) < 17:
    options = options + [0 for i in range(0, 17-len(options))]
df = pd.DataFrame(options)
print(df.T)
print(df.values)
df1 = pd.read_csv(r"D:\Downlaod\New folder\Symptom-severity.csv")
vals = df.values
symptoms = df1['Symptom'].unique()

for i in range(len(symptoms)):
    vals[vals == symptoms[i]] = df1[df1['Symptom'] == symptoms[i]]['weight'].values[0]
df = pd.DataFrame(vals)
print(df)
data = df.values
x = np.array([df[0].tolist()])


disease = ['Diabetes','Bronchial Asthma','Heart attack','Hypertension','Arthritis','Psoriasis']
if (st.button('Find Health Status')):
    feat_cols = pd.DataFrame()

    model = load('soh.h5')
    pred = model.predict(x)
    st.title('According to symptoms the chances of having diseases are:')
    
    lst = []
    for i in pred:
        for j in i:
            lst.append(j)
    chart_data = pd.DataFrame(data = [lst],
    columns=disease)
    st.bar_chart(chart_data)
    st.title(disease[np.argmax(pred)])
