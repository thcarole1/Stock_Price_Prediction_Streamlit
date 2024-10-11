import streamlit as st
import os
import shutil


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

    st.session_state['ticker_entered'] = True
# ***************************************************************************
