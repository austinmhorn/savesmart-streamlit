import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys

sys.path.append('../SaveSmart-streamlit')
 
from modules import get_lesson_quiz
 
COLS = 8
columns = st.columns( COLS )

quiz = get_lesson_quiz('budgeting')
question = quiz['1']['question']
ans = quiz['1']['answers']

with columns[0]:
    if st.button('Back'):
        switch_page("home")
        
# Header
st.markdown("#### Lesson 1: Budgeting Quiz")
st.text("- Question 1/3")
st.write('------------------------------------------------------------------------------------------')


genre = st.radio(
    question,
    [ans[0:1], ans[1:2], ans[2:3], ans[3:4]]
)


with columns[7]:
    if st.button('Finish'):
        switch_page("home")
        