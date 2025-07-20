import streamlit as st
import pandas as pd

# Load the dataset
orders = pd.read_csv("CSV/orders.csv")

# App UI
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")

# Simple Metrics
total_sales = orders['Amount'].sum()
st.metric("Total Sales", f"${total_sales:,.2f}")

# Display raw data
st.subheader("Order Data")
st.dataframe(orders)
