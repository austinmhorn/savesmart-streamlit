import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("""
Financial Aid
""")

if st.button('Back'):
    switch_page("home")