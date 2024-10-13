import streamlit as st
import os
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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
    fig, ax = plt.subplots(figsize=(16,8))

    sns.lineplot(x=y_train_dates,
                 y=y_train['y_train'])
    sns.lineplot(x=y_test_dates,
                 y=y_test['y_test'],
                #  color = '#DCB484',
                 color = 'red',
                 linestyle = '--')
    sns.lineplot(x=y_test_dates,
                 y=y_pred['y_pred'],
                color='#FF961A')

    # Change the figure background color
    # ax.set_facecolor('#18130D') # Set background color of the plot
    # fig.patch.set_facecolor('#18130D') # Set figure background color
    ax.set_facecolor('#000000') # Set background color of the plot
    fig.patch.set_facecolor('#000000') # Set figure background color

    # Set title and its color
    ax.set_title(f'Prediction of {short_name} stock price with LSTM',
                 fontsize=18,
                 color='#EDF0F5')  # Change title color

    plt.legend(['Training data', 'Actual data', 'Predictions'],
               loc='lower right')

    plt.xlabel('Date', fontsize=18)

    # Set Y-axis label and change its color
    ax.set_ylabel(f'Close price in {currency}',
                  fontsize=18,
                  color='#EDF0F5')

    # Set X-axis label and change its color
    ax.set_xlabel('Date',
                  fontsize=18,
                  color='#EDF0F5')

    # Set spines color
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('#EDF0F5')
    ax.spines['bottom'].set_color('#EDF0F5')

    # Set major tick label color
    ax.tick_params(axis='x',colors='#EDF0F5')  # Set X-axis tick label color
    ax.tick_params(axis='y',colors='#EDF0F5')  # Set Y-axis tick label color

    # Set the number of displayed values on the x-axis
    # ax.xaxis.set_major_locator(ticker.MaxNLocator(10))  # Display only 5 x-axis labels

    # Set major ticks to show only years
    ax.xaxis.set_major_locator(mdates.YearLocator(1))  # Show every year
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format to show only the year

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)

def plot_actual_predictions_api(y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Plot stock prices : actual vs predicted (ONLY predictions and actual. No train data displayed) => SEABORN
    fig, ax = plt.subplots(figsize=(16,8))

    sns.lineplot(x=y_test_dates,
                 y=y_test['y_test'],
                #  color = '#DCB484',
                 color = 'red',
                 linestyle = '--')
    sns.lineplot(x=y_test_dates,
                 y=y_pred['y_pred'],
                color='#FF961A')

    # Change the figure background color
    # ax.set_facecolor('#18130D') # Set background color of the plot
    # fig.patch.set_facecolor('#18130D') # Set figure background color
    ax.set_facecolor('#000000') # Set background color of the plot
    fig.patch.set_facecolor('#000000') # Set figure background color

    # Set title and its color
    ax.set_title(f'Prediction of {short_name} stock price with LSTM',
                 fontsize=18,
                 color='#EDF0F5')  # Change title color

    plt.legend(['Actual data', 'Predictions'],
               loc='lower right')

    plt.xlabel('Date', fontsize=18)

    # Set Y-axis label and change its color
    ax.set_ylabel(f'Close price in {currency}',
                  fontsize=18,
                  color='#EDF0F5')

    # Set X-axis label and change its color
    ax.set_xlabel('Date',
                  fontsize=18,
                  color='#EDF0F5')

    # Set spines color
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('#EDF0F5')
    ax.spines['bottom'].set_color('#EDF0F5')

    # Set major tick label color
    ax.tick_params(axis='x',
                   colors='#EDF0F5')  # Set X-axis tick label color
    ax.tick_params(axis='y',
                   colors='#EDF0F5')  # Set Y-axis tick label color

    # Set major ticks to show months and years only
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))  # Show every 2nd month
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to show Year-Month

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)

def plot_actual_predictions_last_values_api(y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Plot stock prices : actual vs predicted (ONLY predictions and actual. No train data displayed) ==> WITH SEABORN
    number_last = 100

    fig, ax = plt.subplots(figsize=(16,8))

    sns.lineplot(x=y_test_dates.iloc[-number_last:],
                 y=y_test['y_test'].iloc[-number_last:],
                #  color = '#DCB484',
                 color = 'red',
                 linestyle = '--')
    sns.lineplot(x=y_test_dates.iloc[-number_last:],
                 y=y_pred['y_pred'].iloc[-number_last:],
                 color='#FF961A')

    # Change the figure background color
    # ax.set_facecolor('#18130D') # Set background color of the plot
    # fig.patch.set_facecolor('#18130D') # Set figure background color
    ax.set_facecolor('#000000') # Set background color of the plot
    fig.patch.set_facecolor('#000000') # Set figure background color

    # Set title and its color
    ax.set_title(f'Prediction of {short_name} stock price with LSTM on the last {number_last} days',
                 fontsize=18,
                 color='#EDF0F5')  # Change title color

    plt.legend(['Actual data', 'Predictions'],
               loc='lower right')

    plt.xlabel('Date', fontsize=18)

    # Set Y-axis label and change its color
    ax.set_ylabel(f'Close price in {currency}',
                  fontsize=18,
                  color='#EDF0F5')

    # Set X-axis label and change its color
    ax.set_xlabel('Date',
                  fontsize=18,
                  color='#EDF0F5')

    # Set spines color
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('#EDF0F5')
    ax.spines['bottom'].set_color('#EDF0F5')

    # Set major tick label color
    ax.tick_params(axis='x',
                   colors='#EDF0F5')  # Set X-axis tick label color
    ax.tick_params(axis='y',
                   colors='#EDF0F5')  # Set Y-axis tick label color

    # Set major ticks to show months and years only
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))  # Show every 10 day
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format to show Year-Month-Day

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)

def plot_display_all(y_train, y_train_dates,\
                                y_test, y_test_dates, y_pred, \
                                short_name, currency):
    # Subplots
    # fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(16,8))
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(16,24))

    # Plot stock prices : training data vs actual vs predicted
    sns.lineplot(x=y_train_dates,
                 y=y_train['y_train'],
                 ax = axes[0])
    sns.lineplot(x=y_test_dates,
                 y=y_test['y_test'],
                #  color = '#DCB484',
                 color = 'red',
                 linestyle = '--',
                 ax = axes[0])
    sns.lineplot(x=y_test_dates,
                 y=y_pred['y_pred'],
                color='#FF961A',
                ax = axes[0])

    # Plot stock prices : actual vs predicted
    sns.lineplot(x=y_test_dates,
                 y=y_test['y_test'],
                #  color = '#DCB484',
                color = 'red',
                linestyle = '--',
                ax = axes[1])
    sns.lineplot(x=y_test_dates,
                 y=y_pred['y_pred'],
                color='#FF961A',
                ax = axes[1])

    # Plot stock prices : actual vs predicted (LIMITED VALUES)
    number_last = 100
    sns.lineplot(x=y_test_dates.iloc[-number_last:],
                 y=y_test['y_test'].iloc[-number_last:],
                #  color = '#DCB484',
                 color = 'red',
                 linestyle = '--',
                ax = axes[2])
    sns.lineplot(x=y_test_dates.iloc[-number_last:],
                 y=y_pred['y_pred'].iloc[-number_last:],
                 color='#FF961A',
                ax = axes[2])

    # Change the figure background color
    fig.patch.set_facecolor('#000000') # Set figure background color
    axes[0].set_facecolor('#000000') # Set background color of the plot
    axes[1].set_facecolor('#000000') # Set background color of the plot
    axes[2].set_facecolor('#000000') # Set background color of the plot

    # Set title and its color
    axes[0].set_title(f'Prediction of {short_name} stock price with LSTM',
                        fontsize=18,
                        color='#EDF0F5')  # Change title color
    axes[1].set_title(f'Prediction of {short_name} stock price with LSTM',
                        fontsize=18,
                        color='#EDF0F5')  # Change title color
    axes[2].set_title(f'Prediction of {short_name} stock price with LSTM on the last {number_last} days',
                        fontsize=18,
                        color='#EDF0F5')  # Change title color

    # Set legend
    axes[0].legend(['Training data', 'Actual data', 'Predictions'],
                   loc='upper left',
                   facecolor = '#000000',
                   labelcolor = '#EDF0F5',
                   edgecolor = '#000000')
    axes[1].legend(['Actual data', 'Predictions'],
                   loc='upper left',
                   facecolor = '#000000',
                   labelcolor = '#EDF0F5',
                   edgecolor = '#000000')
    axes[2].legend(['Actual data', 'Predictions'],
                   loc='upper left',
                   facecolor = '#000000',
                   labelcolor = '#EDF0F5',
                   edgecolor = '#000000')

    # Set X-axis label and change its color
    axes[0].set_xlabel('Date', fontsize=18, color='#EDF0F5')
    axes[1].set_xlabel('Date', fontsize=18, color='#EDF0F5')
    axes[2].set_xlabel('Date', fontsize=18, color='#EDF0F5')

    # Set Y-axis label and change its color
    axes[0].set_ylabel(f'Close price in {currency}',fontsize=18,color='#EDF0F5')
    axes[1].set_ylabel(f'Close price in {currency}',fontsize=18,color='#EDF0F5')
    axes[2].set_ylabel(f'Close price in {currency}',fontsize=18,color='#EDF0F5')

    # Configure grid
    # axes[0].grid(visible = True, linestyle = '--')

    # Set spines color
    axes[0].spines['top'].set_color('none')
    axes[0].spines['right'].set_color('none')
    axes[0].spines['left'].set_color('#EDF0F5')
    axes[0].spines['bottom'].set_color('#EDF0F5')

    axes[1].spines['top'].set_color('none')
    axes[1].spines['right'].set_color('none')
    axes[1].spines['left'].set_color('#EDF0F5')
    axes[1].spines['bottom'].set_color('#EDF0F5')

    axes[2].spines['top'].set_color('none')
    axes[2].spines['right'].set_color('none')
    axes[2].spines['left'].set_color('#EDF0F5')
    axes[2].spines['bottom'].set_color('#EDF0F5')

    # Set major tick label color
    axes[0].tick_params(axis='x',colors='#EDF0F5')  # Set X-axis tick label color
    axes[0].tick_params(axis='y',colors='#EDF0F5')  # Set Y-axis tick label color
    axes[1].tick_params(axis='x',colors='#EDF0F5')  # Set X-axis tick label color
    axes[1].tick_params(axis='y',colors='#EDF0F5')  # Set Y-axis tick label color
    axes[2].tick_params(axis='x',colors='#EDF0F5')  # Set X-axis tick label color
    axes[2].tick_params(axis='y',colors='#EDF0F5')  # Set Y-axis tick label color

    # Set major ticks to show only years
    axes[0].xaxis.set_major_locator(mdates.YearLocator(1))  # Show every year
    axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format to show only the year

    # Set major ticks to show months and years only
    axes[1].xaxis.set_major_locator(mdates.MonthLocator(interval=2))  # Show every 2nd month
    axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to show Year-Month

    # Set major ticks to show days, months and years
    axes[2].xaxis.set_major_locator(mdates.DayLocator(interval=20))  # Show every 20 day
    axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format to show Year-Month-Day

    # Adjust space between subplots
    plt.subplots_adjust(hspace=0.3)  # hspace adjusts the height spacing between rows

    st.pyplot(plt)

def create_summary():
    return  ''
