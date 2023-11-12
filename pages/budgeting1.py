import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys

sys.path.append('../SaveSmart-streamlit')
 
from modules import get_lesson_reading
 
COLS = 8
columns = st.columns( COLS )

reading = get_lesson_reading('budgeting')
spliced_reading = reading[0:2]

with columns[0]:
    if st.button('Back'):
        switch_page("home")
with columns[7]:
    if st.button('Next >'):
        switch_page("budgeting2")
        
# Header
st.markdown("#### Lesson 1: Budgeting")
st.text("- Reading Section 1/2")
st.write('------------------------------------------------------------------------------------------')

for paragraph in spliced_reading:
    st.write(paragraph)
    st.write()