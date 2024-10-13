import streamlit as st
import pandas as pd

from app.delete_create import prepare

from app.api import perform_api_call

from app.data import retrieve_currency_api, \
    retrieve_short_name_api,retrieve_values

from app.display import display_images, display_summary,\
    plot_train_actual_predictions_api,\
    plot_actual_predictions_api,\
    plot_actual_predictions_last_values_api,\
    plot_display_all, create_summary

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Init session_state
if 'ticker_entered' not in st.session_state:
    st.session_state['ticker_entered'] = False

# Explanation of the purpose of this app
st.markdown(
    """
    <h1 class="title">Stock price prediction </h1>
    <h2 class="subtitle"> This app helps users predict a stock price based on its ticker. </h2>
    <h2 class="subtitle"> Based on at least 10-year historical data from Yahoo finance,
        the predictions are based on Deep Learning LSTM cells. </h2>

    <h2 class="subtitle"> Step 1 : The Deep Learning model "learns" the patterns of 8 years of historical data of stock. <br>
                          Step 2 : The Deep Learning model "predicts" the following 2 years of evolution of the considered stock. </h2>
    <h2 class="subtitle"> It’s designed for Stock market enthusiasts looking for an easy way to estimate stock price movement. </h2>
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
        # Retrieve info from api call response (ZIP file)
        currency = retrieve_currency_api()
        short_name = retrieve_short_name_api()
        y_train = retrieve_values('y_train')
        y_test = retrieve_values('y_test')
        y_pred = retrieve_values('y_pred')
        y_train_dates = retrieve_values('y_train_dates')
        y_test_dates = retrieve_values('y_test_dates')

        # Transform dates to datetime
        y_train_dates = y_train_dates.iloc[:,0]
        y_train_dates = pd.to_datetime(y_train_dates)
        y_test_dates = y_test_dates.iloc[:,0]
        y_test_dates = pd.to_datetime(y_test_dates)

        plot_display_all(y_train, y_train_dates,\
                        y_test, y_test_dates, y_pred, \
                        short_name, currency)

        create_summary(y_test, y_pred, y_test_dates)
        st.session_state['ticker_entered'] = False


# currency = retrieve_currency_api()
# short_name = retrieve_short_name_api()
# y_train = retrieve_values('y_train')
# y_test = retrieve_values('y_test')
# y_pred = retrieve_values('y_pred')
# y_train_dates = retrieve_values('y_train_dates')
# y_test_dates = retrieve_values('y_test_dates')

# # Transform dates to datetime
# y_train_dates = y_train_dates.iloc[:,0]
# y_train_dates = pd.to_datetime(y_train_dates)

# y_test_dates = y_test_dates.iloc[:,0]
# y_test_dates = pd.to_datetime(y_test_dates)


# plot_display_all(y_train, y_train_dates,\
#                 y_test, y_test_dates, y_pred, \
#                 short_name, currency)

# create_summary(y_test, y_pred, y_test_dates)
