import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
from matplotlib.backends.backend_agg import RendererAgg

class GraphicGenerator:
    def __init__(self, df):
        self.df = df
        self.columns = df.columns.values
        self.binary_columns = [c for c in self.df[self.columns] if sorted(list(self.df[c].value_counts().index)) == ([0, 1])]
        self._lock = RendererAgg.lock

    def scatterplot(self):
        st.markdown('### Scatter Plots')
        columns_scatter_x = st.multiselect('Columns for the X axis:', self.columns, default=None, key='x_dispersao')
        columns_scatter_y = st.multiselect('Columns for the Y axis:', self.columns, default=None, key='y_dispersao')

        if columns_scatter_x:
            if columns_scatter_y:
                for x_axis in columns_scatter_x:
                    for y_axis in columns_scatter_y:
                        with self._lock:
                            fig = plt.figure(figsize=(13, 9))
                            ax = sns.scatterplot(x=self.df[x_axis], y=self.df[y_axis])
                            ax.set_title(x_axis.capitalize() + ' X ' + y_axis.capitalize())
                            ax.set_ylabel(y_axis.capitalize())
                            ax.set_xlabel(x_axis.capitalize())
                            st.pyplot(fig)

    def correlationPlot(self):
        st.markdown('### Correlations heat map')
        corrMatrix = self.df.corr()
        with self._lock:
            fig = plt.figure(figsize=(13, 9))
            ax = sns.heatmap(corrMatrix, annot=True)
            ax.set_title('Heat map of correlations of variables')
            st.pyplot(fig)

    def pairplot(self):
        st.markdown('### Pairplot')
        columns_pairplot = st.multiselect('Columns: ', self.columns, default=None, key='xy_pairplot')

        if columns_pairplot:
            with self._lock:
                pairplot = sns.pairplot(self.df[columns_pairplot])
                st.pyplot(pairplot)

    def logisticRegressionPlot(self):
        st.markdown('### Logistic Regression Plots')
        columns_regression_x = st.multiselect('Columns for the X axis: ', self.columns, default=None, key='x_reg_log')
        columns_regression_y = st.multiselect('Columns for the Y axis: ', self.binary_columns, default=None, key='y_reg_log')

        if columns_regression_x:
            if columns_regression_y:
                for x_axis in columns_regression_x:
                    for y_axis in columns_regression_y:
                        with self._lock:
                            fig = plt.figure(figsize=(13, 9))
                            ax = sns.regplot(x=self.df[x_axis], y=self.df[y_axis], logistic=True, ci=0, line_kws={"color": "red"})
                            ax.set_title(x_axis.capitalize() + ' X ' + y_axis.capitalize())
                            ax.set_ylabel(y_axis.capitalize())
                            ax.set_xlabel(x_axis.capitalize())
                            st.pyplot(fig)