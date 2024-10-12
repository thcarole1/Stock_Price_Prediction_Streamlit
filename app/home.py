import streamlit as st
import time

from app.delete_create import prepare
from app.api import perform_api_call
from app.data import retrieve_currency_api, \
    retrieve_short_name_api,retrieve_values
from app.display import display_images, display_summary,\
    plot_train_actual_predictions_api,\
    plot_actual_predictions_api,\
    plot_actual_predictions_last_values_api

if 'ticker_entered' not in st.session_state:
    st.session_state['ticker_entered'] = False

#  Formatting
st.markdown(
    """
    <style>

    .stApp {
        background-color: #000000;
    }

    .title {
        text-align: center;
        color : #EDF0F5;
    }
    .subtitle {
        text-align: center;
        color : #EDF0F5;
        # font-size: 1.5em;
        font-size: 1.4em;
    }
    .first-sentence {
        text-align: left;
        margin-top: 20px;
        font-size: 1.2em;
    }

    div[data-testid="stTextInput"] > label {
        color : #EDF0F5;
        font-size: 1.2em;
    }

    .custom-spinner {
        color: orange;  /* Change to your desired color */
        font-size: 20px;  /* Optional: adjust font size */
    }
    </style>

    <h1 class="title">Stock price prediction </h1>
    <h2 class="subtitle"> This app helps users predict a stock price based on its ticker. </h2>
    <h2 class="subtitle"> Based on at least 10-year historical data from Yahoo finance, the predictions are based on  LSTM cells. </h2>
    <h2 class="subtitle"> It’s designed for Stock market enthusiasts looking for an easy way to esimate stock price movement. </h2>
    """,
    unsafe_allow_html=True
)

# Retrieve ticker from user
ticker = st.text_input(label = "Please enter a valid stock ticker :",
              value="",
              max_chars=4,
              key=None,
              type="default",
              on_change=prepare,
              placeholder="AAPL, MSFT, STLA, NVDA, GOOGL, META, TSLA for example")

# Display a loading message while the calculation is in progress
if st.session_state['ticker_entered']:
    with st.spinner("Calculating...."):
        perform_api_call(ticker)
        currency = retrieve_currency_api()
        short_name = retrieve_short_name_api()
        y_train = retrieve_values('y_train')
        y_test = retrieve_values('y_test')
        y_pred = retrieve_values('y_pred')
        y_train_dates = retrieve_values('y_train_dates')
        y_test_dates = retrieve_values('y_test_dates')

        print(f"Shape of y_train : {y_train.shape}")
        print(f"Shape of y_test : {y_test.shape}")
        print(f"Shape of y_pred : {y_pred.shape}")
        print(f"Shape of y_train_dates : {y_train_dates.shape}")
        print(f"Shape of y_test_dates : {y_test_dates.shape}")

        plot_train_actual_predictions_api(y_train, y_train_dates,\
                                        y_test, y_test_dates, y_pred, \
                                        short_name, currency)

        plot_actual_predictions_api(y_test, y_test_dates, y_pred, \
                                short_name, currency)

        plot_actual_predictions_last_values_api(y_test, y_test_dates, y_pred, \
                                short_name, currency)

        # display_images()
        # display_summary()
        st.session_state['ticker_entered'] = False
