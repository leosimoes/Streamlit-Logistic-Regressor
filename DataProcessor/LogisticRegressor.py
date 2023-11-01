import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression


class LogisticRegressor:

    def __init__(_self, df):
        _self.df = df.select_dtypes(include=['number']).dropna()
        _self.columns = _self.df.columns.values
        _self.binary_columns = [c for c in _self.df if sorted(list(_self.df[c].value_counts().index)) == ([0, 1])]

    def logistic(_self):
        X = st.multiselect('X', _self.columns, default=None, key='x_logistic_reg')
        y = st.selectbox('y', _self.binary_columns, key='y_logistic_reg')
        if st.button('Train Logistic Regression'):
            if X:
                if y:
                    # Training the model
                    clf = LogisticRegression(random_state=0)
                    clf.fit(_self.df[X].values, _self.df[[y]].values.ravel())
                    st.write('Training score: ' + str(round(clf.score(_self.df[X].values, _self.df[[y]].values.ravel()), 3)))

                    # Formatting coefficients for printing
                    coefficients_values = clf.coef_[0].tolist() + [clf.intercept_[0]]
                    coefficients_names = X.copy() + ['Constant']
                    coefficients_df = pd.DataFrame([coefficients_values], columns=coefficients_names,
                                                   index=['Coefficients'])

                    st.table(coefficients_df)