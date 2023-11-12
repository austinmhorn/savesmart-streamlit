import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys

sys.path.append('../SaveSmart-streamlit')
 
from modules import get_lesson_reading
 
COLS = 8
columns = st.columns( COLS )

reading = get_lesson_reading('debt')
spliced_reading = reading[2:4]

with columns[0]:
    if st.button('Back'):
        switch_page("debt1")
with columns[7]:
    if st.button('Quiz'):
        switch_page("debtQ1")
        
# Header
st.markdown("#### Lesson 2: Debt")
st.text("- Reading Section 2/2")
st.write('------------------------------------------------------------------------------------------')

for paragraph in spliced_reading:
    st.write(paragraph)
    st.write()