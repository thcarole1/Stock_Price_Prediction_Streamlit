import streamlit as st
import time

from app.delete_create import delete_create_folder, prepare
from app.api import perform_api_call
from app.display import display_images, display_summary

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
        time.sleep(3)
        # perform_api_call(ticker)
        # display_images()
        # display_summary()
        st.session_state['ticker_entered'] = False


# # Display a loading message while the calculation is in progress
# if st.session_state['ticker_entered']:
#     with st.spinner('<span class="custom-spinner">Loading...</span>'):
#         time.sleep(3)
#         # perform_api_call(ticker)
#         # display_images()
#         # display_summary()
#         st.session_state['ticker_entered'] = False


# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)

# for percent_complete in range(100):
#     time.sleep(0.01)
#     my_bar.progress(percent_complete + 1, text=progress_text)
# time.sleep(1)
# my_bar.empty()

# st.button("Rerun")
