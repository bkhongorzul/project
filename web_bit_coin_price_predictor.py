import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from tensorflow.keras.models import load_model
from tensorflow.keras.initializers import Orthogonal

# Define custom objects
custom_objects = {
    'Orthogonal': Orthogonal
}

# Load the model with custom objects
try:
    model = load_model("Latest_bit_coin_model.keras", custom_objects=custom_objects)
    st.write("Model loaded successfully")
except Exception as e:
    st.write("Error loading model:", e)

# Fetch and display Bitcoin data
stock = "BTC-USD"
start = "2020-01-01"
end = "2021-01-01"
bit_coin_data = yf.download(stock, start, end)
st.subheader("Bitcoin Data")
st.write(bit_coin_data)

# Plot the data
plt.figure(figsize=(10, 4))
plt.plot(bit_coin_data['Close'], label='Bitcoin Price')
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
st.pyplot(plt)
