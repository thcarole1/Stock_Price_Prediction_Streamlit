import streamlit as st
import zipfile
import requests

def perform_api_call(ticker : str):
    # st.write(text = f"The chosen ticker is {ticker}.")

    # ************************** Connection to API ***************************************
    # API endpoint
    URL = "https://stockpriceprediction-yyzifgu2zq-od.a.run.app/ticker/"

    # Sending POST request and saving the response as a response object
    r = requests.get(url=URL, params={'query': ticker})


    # *************************  Download ZIP file ****************************************
    # Check if the response contains a ZIP file
    if r.status_code == 200 and r.headers['Content-Type'] == 'application/zip':
        # Save the ZIP file
        with open("raw_data/output.zip", "wb") as file:
            file.write(r.content)
        print("ZIP file downloaded successfully!")
    else:
        print("Failed to download the ZIP file or incorrect response.")

    # ************************** Extract data from ZIP file ******************************
    # Open the ZIP file
    with zipfile.ZipFile('raw_data/output.zip', 'r') as zip_ref:
        # List all files within the ZIP
        file_list = zip_ref.namelist()
        # print("Files in the ZIP:", file_list)

        # Extract all files to the current directory (optional)
        zip_ref.extractall('extracted_data')
    # **************************************************************************
