import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels


class GraphicGenerator:
    def __init__(_self, df):
        _self.df = df
        _self.columns = df.columns.values
        _self.binary_columns = [c for c in _self.df[_self.columns] if sorted(list(_self.df[c].value_counts().index)) == ([0, 1])]

    def scatterplot(_self):
        st.markdown('### Scatter Plots')
        columns_scatter_x = st.multiselect('Columns for the X axis:', _self.columns, default=None, key='x_dispersao')
        columns_scatter_y = st.multiselect('Columns for the Y axis:', _self.columns, default=None, key='y_dispersao')

        if columns_scatter_x:
            if columns_scatter_y:
                for x_axis in columns_scatter_x:
                    for y_axis in columns_scatter_y:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.scatterplot(x=_self.df[x_axis], y=_self.df[y_axis])
                        ax.set_title(x_axis.capitalize() + ' X ' + y_axis.capitalize())
                        ax.set_ylabel(y_axis.capitalize())
                        ax.set_xlabel(x_axis.capitalize())
                        st.pyplot(fig)

    def correlationPlot(_self):
        st.markdown('### Correlations heat map')
        corrMatrix = _self.df.corr()
        fig = plt.figure(figsize=(13, 9))
        ax = sns.heatmap(corrMatrix, annot=True)
        ax.set_title('Heat map of correlations of variables')
        st.pyplot(fig)

    def pairplot(_self):
        st.markdown('### Pairplot')
        columns_pairplot = st.multiselect('Columns: ', _self.columns, default=None, key='xy_pairplot')

        if columns_pairplot:
            pairplot = sns.pairplot(_self.df[columns_pairplot])
            st.pyplot(pairplot)

    def logisticRegressionPlot(_self):
        st.markdown('### Logistic Regression Plots')
        columns_regression_x = st.multiselect('Columns for the X axis: ', _self.columns, default=None, key='x_reg_log')
        columns_regression_y = st.multiselect('Columns for the Y axis: ', _self.binary_columns, default=None, key='y_reg_log')

        if columns_regression_x:
            if columns_regression_y:
                for x_axis in columns_regression_x:
                    for y_axis in columns_regression_y:
                        fig = plt.figure(figsize=(13, 9))
                        ax = sns.regplot(x=_self.df[x_axis], y=_self.df[y_axis], logistic=True, ci=0, line_kws={"color": "red"})
                        ax.set_title(x_axis.capitalize() + ' X ' + y_axis.capitalize())
                        ax.set_ylabel(y_axis.capitalize())
                        ax.set_xlabel(x_axis.capitalize())
                        st.pyplot(fig)