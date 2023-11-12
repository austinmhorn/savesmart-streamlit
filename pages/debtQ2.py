import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.disabled = False

m = st.markdown("<style> div.stButton > button:first-child { background-color: rgb(204, 49, 49); } </style>", unsafe_allow_html=True)

sys.path.append('../SaveSmart-streamlit')
 
from modules import get_lesson_quiz
 
COLS = 8
columns = st.columns( COLS )

quiz = get_lesson_quiz('debt')
question = quiz['2']['question']
ans = quiz['2']['answers']

with columns[0]:
    if st.button('Back'):
        switch_page("debtQ1")
with columns[7]:
    if st.button('Next'):
        switch_page("debtQ3")
        
# Header
st.markdown("#### Quiz - Lesson 2: Debt")
st.text("- Question 2/3")
st.write('------------------------------------------------------------------------------------------')

genre = st.radio(
    question,
    [ans[0], ans[1], ans[2], ans[3]]
)

if st.button('Submit'):
    if genre == ans[0]:
        st.subheader(':green[Correct!]')
    else:
        st.subheader(':red[Incorrect.]')