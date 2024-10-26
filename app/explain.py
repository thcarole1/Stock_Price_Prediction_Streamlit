import streamlit as st

def display_row(data):
    '''    Display content in row     '''
    col_number = 4
    # First row of columns (two columns)
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown(f"""<h2 class="subtitle_2"> {data[0]} </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown(f"""<h2 class="subtitle_2"> {data[1]} </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<h2 class="subtitle_2"> {data[2]} </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<h2 class="subtitle_2"> {data[3]} </h2> """, unsafe_allow_html=True)


def display_row_0():
    '''    Display content in row     '''
    col_number = 4

    # First row of columns (4 columns)
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">Number</h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">Steps</h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">Description</h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">Technologies used</h2> """, unsafe_allow_html=True)

def display_row_1():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">1</h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">Data extraction</h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">Extract data
                        from yFinance API : <br>
                        - Temporal data<br>
                        - Company name<br>
                        - Currency
                        </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                        - yFinance API <br>
                        - Python<br>
                        - Pandas
                        </h2> """, unsafe_allow_html=True)

def display_row_2():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    2
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Data exploration
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    What is the data like ? <br>
                    - Shape <br>
                    - Columns content, <br>
                    - statistical properties, <br>
                    - etc…
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                        - Python <br>
                        - Pandas
                        </h2> """, unsafe_allow_html=True)

def display_row_3():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    3
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Data cleaning <br>
                    and <br>
                    feature engineering
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    Dealing with :<br>
                    - duplicates,<br>
                    - missing data,<br>
                    - outliers, <br>
                    - scaling the data
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - sklearn.preprocessing<br>
                    - matplotlib.pyplot<br>
                    - seaborn<br>
                    - scipy.stats
                    </h2> """, unsafe_allow_html=True)

def display_row_4():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    4
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Define train and test data
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    Define train and test data
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - Numpy
                    </h2> """, unsafe_allow_html=True)

def display_row_5():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    5
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Modeling
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    Model creation with LSTM cells
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - tensorflow.keras: <br>
                    .models <br>
                    .optimizers <br>
                    .layers.LSTM
                    </h2> """, unsafe_allow_html=True)

def display_row_6():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    6
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Training the model
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    Training the model
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - tensorflow.keras: <br>
                    .callbacks.EarlyStopping
                    </h2> """, unsafe_allow_html=True)

def display_row_7():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    7
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Model Evaluation
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    Model Evaluation
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - Sequential().evaluate()
                    </h2> """, unsafe_allow_html=True)

def display_row_8():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    8
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Predictions
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    predict/visualization
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - Matplotlib.pyplot<br>
                    - Seaborn<br>
                    </h2> """, unsafe_allow_html=True)

def display_row_9():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col0:
        st.markdown("""<h2 class="subtitle_2">
                    9
                    </h2> """, unsafe_allow_html=True)
    with col1:
        st.markdown("""<h2 class="subtitle_2">
                    Analysis test data <br>
                    and predictions
                    </h2> """, unsafe_allow_html=True)
    with col2:
        st.markdown("""<h2 class="subtitle_2">
                    Analysis test data <br>
                    and predictions
                    </h2> """, unsafe_allow_html=True)
    with col3:
        st.markdown("""<h2 class="subtitle_2">
                    - describe()<br>
                    - distribution
                    </h2> """, unsafe_allow_html=True)


def display_arrow():
    '''    Display content in row     '''
    col_number = 4
    col0, col1, col2, col3= st.columns(col_number)
    with col1:
        # st.markdown("<span style='color:red; font-size: 24px;'>↗  Red Up-Right Arrow YO</span>", unsafe_allow_html=True)
        # st.markdown("""<span class="arrow_style">
        #                 ↗  Red Up-Right Arrow
        #                 </span>""", unsafe_allow_html=True)

        st.markdown(
                    """
                    <div style="border-left: 3px solid red; height: 20px; display: inline-block; margin-right: 5px;"><span style="font-size:24px;">→</span></div>

                    """,
                    unsafe_allow_html=True)


def display_rows():
    display_row_0()
    display_row_1()
    display_arrow()
    display_row_2()
    display_row_3()
    display_row_4()
    display_row_5()
    display_row_6()
    display_row_7()
    display_row_8()
    display_row_9()



    # # First row of columns (4 columns)
    # col0, col1, col2, col3= st.columns(col_number)
    # with col0:
    #     st.markdown("""<pre class="subtitle">Number</pre> """, unsafe_allow_html=True)
    # with col1:
    #     st.markdown("""<pre class="subtitle_2">Steps</pre> """, unsafe_allow_html=True)
    # with col2:
    #     st.markdown("""<pre class="subtitle_2">Description</pre> """, unsafe_allow_html=True)
    # with col3:
    #     st.markdown("""<pre class="subtitle_2">Technologies used</pre> """, unsafe_allow_html=True)



# data_to_display_1 = ['Number', 'Steps', 'Description', 'Technologies used']
# data_to_display_2 = ['1',
#                     'Data extraction',
#                     'Extract data from yFinance API :\n Temporal data,company name and currency',
#                     'yFinance API, Python, Pandas']
