import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.initializers import Orthogonal

# Define custom objects if any
custom_objects = {
    'Orthogonal': Orthogonal
}

# Load and compile the model
try:
    model = load_model("Latest_bit_coin_model.keras", custom_objects=custom_objects, compile=False)
    model.compile(optimizer=Adam(), loss='mean_squared_error', metrics=['accuracy'])
    st.write("Model loaded and compiled successfully")
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
