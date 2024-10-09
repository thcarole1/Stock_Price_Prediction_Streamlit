import streamlit as st
import os
import zipfile
import requests
from PIL import Image
import numpy as np
import pandas as pd
import shutil

# Initialize the presence of a ticker to False
if 'ticker_entered' not in st.session_state:
    st.session_state['ticker_entered'] = False

# Initialize predicting phase to False
if 'prediction_done' not in st.session_state:
    st.session_state['prediction_done'] = False

# *********  Erase and create folder  **************************************
def delete_create_folder(folder_name):
    # Delete folder if it exists
    folder_exists = os.path.exists(folder_name)
    if folder_exists:
        # Remove a directory and all its contents
        shutil.rmtree(folder_name)
        # print(f"Folder '{folder_name}' deleted successfully.")

    # Create folder
    os.mkdir(folder_name)
    # print(f"Folder '{folder_name}' created successfully.")
# ***************************************************************************

# **********  Function is launched when ticker is entered by user ***************
def prepare():
    # *********  Erase and create folder  ***************************************
    delete_create_folder('raw_data')
    delete_create_folder('extracted_data')
    # ***************************************************************************
    print('delete and create are done')

    # Set the presence of a ticker to True
    st.session_state['ticker_entered'] = True
    # print(st.session_state)
# ***************************************************************************

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 1.5em;
    }
    .first-sentence {
        text-align: left;
        margin-top: 20px;
        font-size: 1.2em;
    }
    </style>

    <h1 class="title">Stock price prediction </h1>
    <h2 class="subtitle">Based on Yahoo Finance information, what are the predictions of a stock price ?</h2>
    """,
    unsafe_allow_html=True
)

# Retrieve ticker from user
ticker = st.text_input("Please enter a valid stock ticker :",
              value="",
              max_chars=4,
              key=None,
              type="default",
              on_change=prepare,
              placeholder="AAPL, MSFT, STLA for example")

if st.session_state['ticker_entered']:
    st.write(f"The chosen ticker is {ticker}.")

# ************************** Connection to API ***************************************
# API endpoint
URL = "https://stockpriceprediction-yyzifgu2zq-od.a.run.app/ticker/"

# Sending POST request and saving the response as a response object
r = requests.get(url=URL, params={'query': ticker})

# st.write(r.status_code)

# Check if the response contains a ZIP file
if r.status_code == 200 and r.headers['Content-Type'] == 'application/zip':
    # Save the ZIP file
    with open("raw_data/output.zip", "wb") as file:
        file.write(r.content)
    print("ZIP file downloaded successfully!")
else:
    print("Failed to download the ZIP file or incorrect response.")

# Open the ZIP file
with zipfile.ZipFile('raw_data/output.zip', 'r') as zip_ref:
    # List all files within the ZIP
    file_list = zip_ref.namelist()
    # print("Files in the ZIP:", file_list)

    # Extract all files to the current directory (optional)
    zip_ref.extractall('extracted_data')
# **************************************************************************

# ******************** Display images ***********************************
# Load your images
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

# **************** Display dataframe ***************************************
path_to_csv = "extracted_data/summary.csv"
summary = pd.read_csv(path_to_csv)
summary = summary.set_index(keys = 'index')
st.write(summary)

# **************************************************************************

st.write("The end !!!")
