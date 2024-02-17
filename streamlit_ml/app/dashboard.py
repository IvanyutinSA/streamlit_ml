import pandas as pd
from os.path import realpath, dirname
import sys
if dirname(dirname(dirname(realpath(__file__)))) not in sys.path:
    sys.path.append(dirname(dirname(dirname(realpath(__file__)))))

import streamlit as st
import streamlit_ml.lib.test.test as ts

from streamlit_ml.lib.models import model_selection, model_estimate

dataset = 'None'
model = 'None'
metrics = []

# with st.sidebar:
#     st.title('Lab')
#     st.selectbox('Choose lab number', [1, 2, 3, 4])

with st.sidebar:
    st.title('Target type')
    target_type = st.selectbox('Choose target variable type', ['Real', 'Categorical'])

dataset = 'wine' if target_type == 'Real' else 'airlines'

# Data
st.sidebar.title("Data")
with st.sidebar.expander('Dataset', expanded=True):
    uploaded_file = ts.upload('Load csv data')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.DataFrame()

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







