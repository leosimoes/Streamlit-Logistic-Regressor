import streamlit as st
import numpy as np
import pandas as pd

class DataEvaluator:
    def __init__(_self, df):
        _self.df = df

    def show_head(_self):
        # Displaying the header and the first lines of the dataframe
        st.write('The header and first lines of the dataset are: ')
        st.dataframe(_self.df.head(10))

    def show_dimensions(_self):
        # Displaying the dataframe dimensions
        dimensions = 'The dimensions of the dataset are ' + str(_self.df.shape[0]) + ' rows and ' + str(
            _self.df.shape[1]) + ' columns.'
        st.write(dimensions)

    def show_columns(_self):
        # Displaying column names
        columns_names = ', '.join(list(_self.df.columns))
        st.write('The columns are: ' + columns_names + '.')
