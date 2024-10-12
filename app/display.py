import streamlit as st
import os
import zipfile
import requests
from PIL import Image
import numpy as np
import pandas as pd
import shutil
import matplotlib.pyplot as plt

def display_images():
    # ******************** Display images ***********************************
    # Load your images
    folder_name = "extracted_data/data/processed_data"
    folder_exists = os.path.exists(folder_name)
    if folder_exists:
        train_test_pred_image = Image.open("extracted_data/data/processed_data/train_test_pred.png")
        test_pred_image = Image.open("extracted_data/data/processed_data/test_pred.png")
        test_pred_limited_image = Image.open("extracted_data/data/processed_data/test_pred_limited.png")

        # Display the image in Streamlit
        st.image(train_test_pred_image,
                caption='train_test_pred_image',
                use_column_width=True)

        st.image(test_pred_image,
                caption='test_pred_image',
                use_column_width=True)

        st.image(test_pred_limited_image,
                caption='test_pred_limited_image',
                use_column_width=True)
    # **************************************************************************

def display_summary():
    # **************** Display dataframe ***************************************
    path_to_csv = "extracted_data/summary.csv"
    summary = pd.read_csv(path_to_csv)
    summary = summary.set_index(keys = 'index')
    st.write(summary)
    # **************************************************************************

def plot_actual_predictions_api(y_train, y_train_dates,\
                                y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Plot stock prices : actual vs predicted
    plt.figure(figsize=(16,8))
    plt.title(f'Prediction of {short_name} stock price with LSTM')
    plt.plot(y_train_dates, y_train)
    plt.plot(y_test_dates, y_test)
    plt.plot(y_test_dates, y_pred)
    plt.legend(['Training data', 'Actual data', 'Predictions'], loc='lower right')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel(f'Close price in {currency}', fontsize=18)
    plt.show()
