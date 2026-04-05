import streamlit as st
import pandas as pd

st.title("AI Cloud Cost Optimizer 💰")

st.write("Welcome! Your app is running successfully 🚀")

# Sample data
data = {
    "Day": [1, 2, 3, 4, 5],
    "Cost": [100, 150, 120, 180, 200]
}

df = pd.DataFrame(data)

st.subheader("Cost Trend")
st.line_chart(df.set_index("Day"))