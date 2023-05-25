import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models
hypertension_model = pickle.load(open('hypertension_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

stroke_model = pickle.load(open('stroke_model.sav','rb'))

# creating a function for hypertension prediction
def hypertension_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = hypertension_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person has no hypertension'
    else:
        return 'The person has hypertension'

# creating a function for heart disease prediction
def heart_disease_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = heart_disease_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person has no heart diseaae'
    else:
        return 'The person has heart disease'


# creating a function for stroke prediction
def stroke_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = stroke_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person has no stroke'
    else:
        return 'The person has stroke'



#sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', ['Hypertension Prediction', 'Heart Disease Prediction', 'Stroke Prediction'],
        icons =['heart-pulse', 'heart', 'person-heart'] ,
        default_index = 0)


#Hypertension Prediction Page
if(selected == 'Hypertension Prediction'):
    #page title
    st.title('Hypertension Prediction')

    #taking input from user
    ID = st.text_input('Unique ID')
    Age = st.text_input('Age of the Person')
    Glucose = st.text_input('Glucose Level')
    BMI = st.text_input('BMI value')

 
    # code for Prediction
    hypertension_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Hypertension Test Result'):
        hypertension_diagnosis = hypertension_prediction([ID, Age, Glucose, BMI])


    st.success(hypertension_diagnosis)

#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction')

    #taking input from user
    ID = st.text_input('Unique ID')
    Age = st.text_input('Age of the Person')
    Glucose = st.text_input('Glucose Level')
    BMI = st.text_input('BMI value')

    # code for Prediction
    heart_disease_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_disease_diagnosis = heart_disease_prediction([ID, Age, Glucose, BMI])
        
    st.success(heart_disease_diagnosis)

#Stroke Prediction Page
if(selected == 'Stroke Prediction'):
    #page title
    st.title('Stroke Prediction')

    #taking input from user
    ID = st.text_input('Unique ID')
    Age = st.text_input('Age of the Person')
    Glucose = st.text_input('Glucose Level')
    BMI = st.text_input('BMI value')

    # code for Prediction
    stroke_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Stroke Test Result'):
        stroke_diagnosis = stroke_prediction([ID, Age, Glucose, BMI])
        
    st.success(stroke_diagnosis)
