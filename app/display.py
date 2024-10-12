import streamlit as st
import os
import zipfile
import requests
from PIL import Image
import numpy as np
import pandas as pd
import seaborn as sns
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

def plot_train_actual_predictions_api(y_train, y_train_dates,\
                                y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Plot stock prices : actual vs predicted
    plt.figure(figsize=(16,8))
    plt.title(f'Prediction of {short_name} stock price with LSTM')
    sns.lineplot(x=y_train_dates['y_train_dates'], y=y_train['y_train'])
    sns.lineplot(x=y_test_dates['y_test_dates'], y=y_test['y_test'])
    sns.lineplot(x=y_test_dates['y_test_dates'], y=y_pred['y_pred'])
    plt.legend(['Training data', 'Actual data', 'Predictions'], loc='lower right')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel(f'Close price in {currency}', fontsize=18)
    st.pyplot(plt)

def plot_actual_predictions_api(y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Plot stock prices : actual vs predicted (ONLY predictions and actual. No train data displayed) => SEABORN
    plt.figure(figsize=(16,8))
    plt.title(f'Prediction of {short_name} stock price with LSTM')
    sns.lineplot(x=y_test_dates['y_test_dates'], y=y_test['y_test'])
    sns.lineplot(x=y_test_dates['y_test_dates'], y=y_pred['y_pred'])
    plt.legend(['Actual data', 'Predictions'], loc='lower right')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel(f'Close price in {currency}', fontsize=18)
    st.pyplot(plt)

def plot_actual_predictions_last_values_api(y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Plot stock prices : actual vs predicted (ONLY predictions and actual. No train data displayed) ==> WITH SEABORN
    number_last = 100

    plt.figure(figsize=(16,8))
    plt.title(f'Prediction of {short_name} stock price with LSTM on the last {number_last} days')
    sns.lineplot(x=y_test_dates['y_test_dates'].iloc[-number_last:], y=y_test['y_test'].iloc[-number_last:])
    sns.lineplot(x=y_test_dates['y_test_dates'].iloc[-number_last:], y=y_pred['y_pred'].iloc[-number_last:])
    plt.legend(['Actual data', 'Predictions'], loc='lower right')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel(f'Close price in {currency}', fontsize=18)
    st.pyplot(plt)
