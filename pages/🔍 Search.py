import streamlit as st
import pandas as pd
from datetime import date


customers_data = pd.read_csv("customers.csv")

st.set_page_config(
    page_title="Registered customers",
    page_icon="📌"
)

st.header("Search in Registered Customers &mdash; :coffee:",  divider='rainbow')

st.data_editor(customers_data)

