import pandas as pd
import os

def retrieve_currency_api():
    '''
    This function retrieves the currency in which the stock is traded in.
    Source is Yahoo Finance.
    Returns a string corresponding to the currency.
    '''

    folder_name = "extracted_data/basic_info.csv"
    folder_exists = os.path.exists(folder_name)
    if folder_exists:
        # **************** Display dataframe ***************************************
        path_to_csv = "extracted_data/basic_info.csv"
        data_df = pd.read_csv(path_to_csv)
        currency = data_df['currency'][0]
        # ************************************************************
        print("✅ Currency has been retrieved.")
        return currency
    return 'No feedback for currency'

def retrieve_short_name_api():
    '''
    This function retrieves the name of the company from yahoo Finance.
    Returns a string.
    '''
    folder_name = "extracted_data/basic_info.csv"
    folder_exists = os.path.exists(folder_name)
    if folder_exists:
        # **************** Display dataframe ***************************************
        path_to_csv = "extracted_data/basic_info.csv"
        data_df = pd.read_csv(path_to_csv)
        short_name = data_df['short_name'][0]
        # ************************************************************
        print("✅ Short_name has been retrieved.")
        return short_name
    return 'No feedback for short_name'

def retrieve_values(name : str):
    folder_name = f"extracted_data/{name}_export.csv"
    folder_exists = os.path.exists(folder_name)
    if folder_exists:
        # path_to_csv = "extracted_data/basic_info.csv"
        path_to_csv  = folder_name
        print(f"✅ dataframe {name} has been retrieved.")
        return pd.read_csv(path_to_csv)
    return 'No feedback for these values'
