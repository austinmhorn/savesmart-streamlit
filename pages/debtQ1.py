import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys

sys.path.append('../SaveSmart-streamlit')
 
from modules import get_lesson_quiz
 
COLS = 8
columns = st.columns( COLS )
result = ""

quiz = get_lesson_quiz('debt')
question = quiz['1']['question']
ans = quiz['1']['answers']

with columns[0]:
    if st.button('Back'):
        switch_page("debt2")
with columns[7]:
    if st.button('Next', disabled=False):
        switch_page("debtQ2")
        

# Header
st.markdown("#### Quiz - Lesson 2: Debt")
st.text("- Question 1/3")
st.write('------------------------------------------------------------------------------------------')

answer = st.radio(
    question,
    [ans[0], ans[1], ans[2], ans[3]]
)

if st.button('Submit'):
    if answer == ans[0]:
        st.subheader(':green[Correct!]')
    else:
        st.subheader(':red[Incorrect.]')