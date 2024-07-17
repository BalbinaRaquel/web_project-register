import streamlit as st
import pandas as pd
from datetime import date



def salving_data(customer_name, birth_date, customer_type, contact_option, customer_email, customer_homephone, customer_mobilephone):
    if customer_name and birth_date <= date.today():
        with open("customers.csv", "a", encoding="utf-8") as file:
            file.write(f"{customer_name}, {birth_date}, {customer_type}, {contact_option}, {customer_email}, {customer_homephone}, {customer_mobilephone}\n") 
        st.session_state["Success"] = True
    else:
        st.session_state["Success"] = False



st.set_page_config(
    page_title="Customer Registration",
    page_icon="🛒"
)

st.header("Customer Registration &mdash; :star:",  divider='rainbow')

# Calender adjustment

date_today = date.today()
date_min = date(1960, 1, 1)
date_max = date_today


customer_name = st.text_input("Enter with your name:",
                            placeholder="Type your name...",
                            key="customer_name")


birth_date = st.date_input("What's your date of birth:",
                            date_max, date_min,
                            format="MM/DD/YYYY",
                            key="customer_birth")


customer_type = st.selectbox("Customer type:", 
                             ["Natural person", "Legal person"],
                              index=None)


contact_option = st.selectbox("How would you like to be contacted?",
                            ("Email", "Home phone", "Mobile phone"),
                            index=None,
                            placeholder="Select contact method...",
                            key="contact_option")

st.write(f"You selected: :green[{contact_option}]")


customer_email = st.text_input("Enter with your E-mail:",
                               value=None, 
                               placeholder="Type a valid E-mail...",
                               key="customer_email")

customer_homephone = st.number_input("Enter with your Home phone:",
                                     value=None, 
                                     placeholder="Type a phone number...",
                                     key="home_phone"
                                    )

customer_mobilephone = st.number_input("Enter with your Mobile phone:",
                                     value=None, 
                                     placeholder="Type a phone number...",
                                     key="mobile_phone"
                                    )

btn_register = st.button('Register customer',
                         on_click=salving_data,
                         args=[customer_name, birth_date, customer_type, 
                               contact_option, customer_email, 
                               customer_homephone, customer_mobilephone])


if btn_register:
    if st.session_state["Success"]:
        st.success(" Customer successfully registered!",
                   icon="✔")
    else:
        st.error(" There was an error in the registration!",
                 icon="❌") 
        st.warning(" Try again!",
                 icon="⚠")    

                                            







