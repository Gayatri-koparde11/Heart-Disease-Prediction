import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models



heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav',  'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu(' Disease Prediction System and CVD Prevention',

                           ['Heart Disease Prediction',
                            'Healthy Heart Strategies'],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)




# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Gender(1=Male, 0=Female)')

    with col3:
        cp = st.text_input('Chest Pain types(0-3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl,(1=true,0=false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved(thalach)')

    with col3:
        exang = st.text_input('Exercise Induced Angina(exang) 1=yes; 0=no')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise(oldpeak)')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy(ca)')

    with col1:
        thal = st.text_input('thal: 0,3 = normal; 1 = fixed defect; 2 = reversable defect; ')

    # code for Prediction
    heart_diagnosis = ''
    Precautions = ''
    

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having risk of heart disease'
            Precautions = 'PRECAUTIONS for Healthy Heart:\n\n 1.Consume Heart-healthy food diet : \n\n Fruits and leafy Vegetables , Whole Grains, Nonfat and low-fat dairy, Healthy Proteins\n\n 2.Foods to avoid for heart health :\n\n Foods and beverages with added sugars, avoid alcohols ,processed foods\n\n  3.Regular Exercise :\n\nAerobic , Stretching Muscles ,Sleep atleast 8 hours a day'
    
        else:
    
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    st.success(Precautions)

if selected ==  "Healthy Heart Strategies":

    Strategies = ''
    
    if st.button('Strategies for Healthy Heart'):

        Strategies = '1.Whatever your diagnosis, the best way to prevent future cardiovascular problems is to get regular exercise\n\n 2.Get moving: Aim for at least 30 to 60 minutes of activity daily\n\n 3.Eat a heart-healthy diet like (fruits and vegetables , low fat for fat free daily products, Healthy fats such as olive oil,whole grains)\n\n 4.Maintain a healthy weight\n\n 5.Get quality sleep\n\n 6.Manage stress\n\n 7.Get regular health screening tests'

    
    st.success(Strategies)


