import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🏠 Home Page - Streamlit Docker App")
st.write("Welcome to the Dockerized Streamlit Application!")

# Data Upload
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(data.head())

    # Visualization
    st.subheader("📊 Data Visualization")
    plt.figure(figsize=(6, 4))
    plt.plot(data.iloc[:, 0], data.iloc[:, 1], marker='o')
    st.pyplot(plt)
