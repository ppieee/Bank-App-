import streamlit as st

st.set_page_config(page_title='Bank App', layout="centered")
st.title('Banking App')

if st.button('Savings Account'):
    st.switch_page('pages/Savings.py')

if st.button('Current Account'):
    st.switch_page('pages/Current.py')



