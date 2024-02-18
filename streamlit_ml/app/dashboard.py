import pandas as pd
from os.path import realpath, dirname
import sys
if dirname(dirname(dirname(realpath(__file__)))) not in sys.path:
    sys.path.append(dirname(dirname(dirname(realpath(__file__)))))

import streamlit as st
import streamlit_ml.lib.test.test as ts

from streamlit_ml.lib.models import model_selection, model_estimate, model_evaluation
from streamlit_ml.lib.dataprep import clean, transform

dataset = 'None'
model = 'None'
metrics = []
target_type = 'None'

# with st.sidebar:
#     st.title('Lab')
#     st.selectbox('Choose lab number', [1, 2, 3, 4])

with st.sidebar:
    st.title('Target type')
    target_type = st.selectbox('Choose target variable type', ['Categorical', 'Real'])

dataset = 'wine' if target_type == 'Real' else 'airlines'

# Data
st.sidebar.title("Data")
with st.sidebar.expander('Dataset', expanded=True):
    uploaded_file = ts.upload('Load csv data')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv('~/Projects/ML/notebooks/7th lab/airlines.csv')[:10_000]

# Model selection
st.sidebar.title('Model')

model_list = model_selection.get_available_models(target_type)
model = st.sidebar.selectbox('Choose model', model_list)

# Hyper parameter selection
st.sidebar.title('Hyperparameters')
with st.sidebar.expander('Choose grid hyperparameters. You can input multiple values with separator \";\"', expanded=False):
    grid_params = model_selection.get_hyperparameters()


# Metrics selection
st.sidebar.title('Metrics')
with st.sidebar.expander('Choose metrics'):
    metrics = model_estimate.get_metrics(target_type)


if df.empty:
    sys.exit()


# bing bang boom

clean.remove_duplicates_and_nulls(df)
X_train, X_test, y_train, y_test = transform.get_train_test_split(df, dataset)
estimator = model_evaluation.get_estimator(model)
estimator = model_evaluation.fit(estimator, X_train, y_train, target_type, grid_params)
y_pred = model_evaluation.predict(estimator, X_test)

model_estimate.display_params(estimator)
model_estimate.display_metrics(y_test, y_pred, metrics)

