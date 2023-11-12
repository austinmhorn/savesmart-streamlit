import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

m = st.markdown(" <style> div.stButton > button:first-child { background-color: rgb(0, 0, 200); width: 240px; } </style>", unsafe_allow_html=True)

st.markdown(' #   *SaveSmart* ')
st.write("--  Financial Investment Coach --")

if st.button('Lesson 1: Budgeting'):
    switch_page("budgeting1")
if st.button('Lesson 2: Debt'):
    switch_page("debt1")
if st.button('Lesson 3: Credit Cards :lock:', disabled=True):
    switch_page("credit_cards")
if st.button('Lesson 4: Financial Aid :lock:', disabled=True):
    switch_page("financial_aid")
if st.button('Lesson 5: Stock Market :lock:', disabled=True):
    switch_page("stock_market")
if st.button('Lesson 6: Retirement Plans :lock:', disabled=True):
    switch_page("retirement_plans")
if st.button('Lesson 7: Cryptocurrency :lock:', disabled=True):
    switch_page("cryptocurrency")