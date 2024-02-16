import streamlit as st
import pandas as pd
import missingno as msno
from streamlit_extras.switch_page_button import switch_page

if 'target' not in st.session_state:
    st.session_state['target'] = ''

st.set_page_config(page_title='The Machine Learning App',
    layout='wide')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('Data preparation')

df =  pd.DataFrame(st.session_state['df'])

def Choose_target_variable():
    st.header('Choose target variable')

    col1, col2 = st.columns(2)
    st.session_state['target'] = col1.selectbox('select:', options= df.columns[1:])
    col1.text('Target Variable: ' + st.session_state['target'])
    col2.write(df[st.session_state['target']].describe())

def Exploratory_data_analysis(df):
    st.header('Exploratory data analysis')
   
    st.write(df.describe(include='all'))
    st.text('Data frame shape: ' + str(df.shape[0]) + " x " + str(df.shape[1]))
    
    st.subheader('Duplicated')
    st.write(df[df.duplicated()])
    st.text('duplicated: ' + str(len(df[df.duplicated()])))

    df = df.drop_duplicates()
    st.text('Data frame shape after cleaning: ' + str(df.shape[0]) + " x " + str(df.shape[1]))

    st.subheader('Missing values in %')
    missing_values = ((df.isna().sum() / len(df)) * 100).sort_values()
    st.table(missing_values.T)

    df_clean = df.copy()

if not pd.DataFrame(st.session_state['df']).empty :
    
    #Choose_target_variable()
    st.write('---')
    Exploratory_data_analysis(df)
    

else:
    click = st.button('Upload data')
    if click:
        switch_page('upload data')
