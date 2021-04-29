import streamlit as st
import numpy as np
import pandas as pd

class DataEvaluator:
    def __init__(self, df):
        self.df = df

    def show_head(self):
        # Displaying the header and the first lines of the dataframe
        st.write('The header and first lines of the dataset are: ')
        st.dataframe(self.df.head(10))

    def show_dimensions(self):
        # Displaying the dataframe dimensions
        dimensions = 'The dimensions of the dataset are ' + str(self.df.shape[0]) + ' rows and ' + str(
            self.df.shape[1]) + ' columns.'
        st.write(dimensions)

    def show_columns(self):
        # Displaying column names
        columns_names = ', '.join(list(self.df.columns))
        st.write('The columns are: ' + columns_names + '.')
