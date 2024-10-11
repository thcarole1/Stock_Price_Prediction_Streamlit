import streamlit as st
import os
import zipfile
import requests
from PIL import Image
import numpy as np
import pandas as pd
import shutil

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
