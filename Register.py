import streamlit as st
import pandas as pd
from datetime import date




def salving_data(customer_name, birth_date, customer_type):
    if customer_name and birth_date <= date.today():
        st.session_state["Success"] = True
    else:
        st.session_state["Success"] = False



st.set_page_config(
    page_title="Customer Registration",
    page_icon="🛒"
)

st.header("Customer Registration", divider='rainbow')


customer_name = st.text_input("Enter with the customer's name:",
                            key="customer_name")

birth_date = st.date_input("Date of birth:", format="DD/MM/YYYY",
                           key="customer_birth")

customer_type = st.selectbox("Customer type:", 
                             ["Natural person", "Legal person"],
                              index=None)

btn_register = st.button('Register customer',
                         on_click=salving_data,
                         args=[customer_name, birth_date, customer_type])


if btn_register:
    if st.session_state["Success"]:
        st.success(" Customer successfully registered!",
                   icon="✔")
    else:
        st.error(" There was an error in the registration!",
                 icon="❌")    

                                            







