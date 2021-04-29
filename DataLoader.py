import streamlit as st
import pandas as pd
import base64


class DataLoader:
    def __init__(self):
        self.is_without_labels = False
        self.separator = ','

    def check_labels(self):
        if st.checkbox('The file has no labels for columns in the first row'):
            self.is_without_labels = True

    def check_separator(self):
        sep_dict = {'comma': ',', 'semicolon': ';', 'space': ' ','tab':'\t'}
        sep = st.selectbox('Select the separator used in the file', list(sep_dict.keys()))
        if sep:
            self.separator = sep_dict[sep]

    def load_file(self):
        return st.file_uploader('Upload csv, tsv or txt file:', type=['csv','tsv','txt'])

    @st.cache
    def load_data(self, arquivo):
        if self.is_without_labels:
            df = pd.read_csv(arquivo, sep=self.separator, header=None)
            df = df.select_dtypes(include=['number'])
            df.dropna(inplace=True)
            df.columns = ['x' + str(i) for i in range(1, df.shape[1] + 1)]
            return df
        else:
            df = pd.read_csv(arquivo, sep=self.separator)
            df = df.select_dtypes(include=['number'])
            df.dropna(inplace=True)
            lowercase = lambda x: str(x).lower()
            df.rename(lowercase, axis='columns', inplace=True)
            return df