import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame()

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

st.title('Upload data')

@st.cache_data(show_spinner="Creating data frame from file...")
def load_data(file):
    df = pd.read_csv(file)
    return df

uploaded_file = st.file_uploader("", type=["csv","xlsx","xls"], key='file_uploader')


if uploaded_file is not None:
    df = load_data(uploaded_file) 
    st.session_state['df'] = df
    st.markdown('Dataset')
    st.write(df.head())
    click = st.button('Next')
    if click:
        switch_page('data preparation')
else:
    st.info('Awaiting for file to be uploaded.')
