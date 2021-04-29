import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

class LogisticRegressor:

    def __init__(self, df):
        self.df = df.select_dtypes(include=['number']).dropna()
        self.columns = self.df.columns.values
        self.binary_columns = [c for c in self.df if sorted(list(self.df[c].value_counts().index)) == ([0, 1])]

    def logistic(self):
        X = st.multiselect('X', self.columns, default=None, key='x_logistic_reg')
        y = st.selectbox('y', self.binary_columns, key='y_logistic_reg')
        if st.button('Train Logistic Regression'):
            if X:
                if y:
                    # Training the model
                    clf = LogisticRegression(random_state=0)
                    clf.fit(self.df[X].values, self.df[[y]].values.ravel())
                    st.write('Training score: ' + str(round(clf.score(self.df[X].values, self.df[[y]].values.ravel()),3)))
                    # Formatting coefficients for printing
                    coefficients_values = np.append(clf.coef_, clf.intercept_)
                    coefficients_df = pd.DataFrame(coefficients_values).T
                    coefficients_names = X.copy()
                    coefficients_names.append('Constant')
                    coefficients_df.columns = coefficients_names
                    coefficients_df.index = ['Coefficients']
                    st.table(coefficients_df)


