import streamlit as st
import os
import zipfile
import requests
from PIL import Image
import numpy as np
import pandas as pd
import shutil



# *********  Erase and create folder  **************************************
def delete_create_folder(folder_name):
    # Delete folder if it exists
    folder_exists = os.path.exists(folder_name)
    if folder_exists:
        # Remove a directory and all its contents
        shutil.rmtree(folder_name)
        print(f"Folder '{folder_name}' deleted successfully.")

    # Create folder
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully.")

# *********  Erase and create folder  *********
delete_create_folder('raw_data')
delete_create_folder('extracted_data')
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

# ************************** Connection to API ***************************************
# Retrieve ticker from user
ticker = st.text_input("Please enter a stock ticker :",
              value="",
              max_chars=4,
              key=None,
              type="default",
              on_change=None,
              placeholder="AAPL for example")

st.write("The chosen ticker is ", ticker)

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
    print("Files in the ZIP:", file_list)

    # Extract all files to the current directory (optional)
    zip_ref.extractall('extracted_data')

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


st.write("The end !!!")
