import streamlit as st
from DataLoader import DataLoader
from DataEvaluator import DataEvaluator
from GraphicGenerator import GraphicGenerator
from LogisticRegressor import LogisticRegressor

# To run the APP: streamlit run streamlit_app.py
if __name__ == '__main__':
    st.header('Logistic Regression')
    st.markdown('*Author: Leonardo Simões*')

    # Data Loader
    st.header('Data loader')
    dataLoader = DataLoader()
    dataLoader.check_labels()
    dataLoader.check_separator()
    file = dataLoader.load_file()

    if file is not None:
        df = dataLoader.load_data(file)

        # Data evaluation
        st.header('Data evaluation')
        st.write('Non-numeric columns and rows with missing values have been dropped.')
        dataEvaluator = DataEvaluator(df)
        dataEvaluator.show_head()
        dataEvaluator.show_dimensions()
        dataEvaluator.show_columns()

        # Graphic Plots
        st.header('Graphic Plots')
        plotGenerator = GraphicGenerator(df)

        checked_pairplot = st.checkbox('PairPlot')
        checked_scatterPlot = st.checkbox('ScatterPlot')
        checked_correlationPlot = st.checkbox('Correlation')
        checked_logisticRegPlot = st.checkbox('LogisticRegPlot')

        if checked_pairplot:
            plotGenerator.pairplot()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if checked_scatterPlot:
            plotGenerator.scatterplot()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if checked_correlationPlot:
            plotGenerator.correlationPlot()
            st.markdown('<hr/>', unsafe_allow_html=True)

        if checked_logisticRegPlot:
            plotGenerator.logisticRegressionPlot()
            st.markdown('<hr/>', unsafe_allow_html=True)

        # Logistic Regression
        st.header('Logistic Regression')
        regressor = LogisticRegressor(df)
        regressor.logistic()
        st.markdown('<hr/>', unsafe_allow_html=True)
