import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(204, 49, 49);
}
</style>""", unsafe_allow_html=True)

st.write("""
# SaveSmart
""")

st.write("""
The #1 Financial Investment Coach 
""")

if st.button('Lesson 1: Budgeting'):
    switch_page("budgeting1")
if st.button('Lesson 2: Debt'):
    switch_page("debt")
if st.button('Lesson 3: Credit Cards'):
    switch_page("credit_cards")
if st.button('Lesson 4: Financial Aid'):
    switch_page("financial_aid")
if st.button('Lesson 5: Stock Market'):
    switch_page("stock_market")
if st.button('Lesson 6: Retirement Plans'):
    switch_page("retirement_plans")
if st.button('Lesson 7: Cryptocurrency'):
    switch_page("cryptocurrency")
