import streamlit as st

def get_available_models(target_type):
    mls = {
        'Real': ['KNeighboursRegressor'],
        'Categorical': ['KNeighboursClassifier'],
    }
    return mls.get(target_type, [])

def get_available_model_hyperparameters(model):
    parameters = {}
    match model:
        case 'KNeighboursClassifier':
            n_neighbors = st.number_input('n_neighbors')
            algorithm = st.selectbox('algorithm', ['auto', 'ball_tree', 'kd_tree', 'brute'])
            leaf_size = st.number_input('leaf_size')
        case 'KNeighboursRegressor':
            n_neighbors = st.number_input('n_neighbors')
            algorithm = st.selectbox('algorithm', ['auto', 'ball_tree', 'kd_tree', 'brute'])
            leaf_size = st.number_input('leaf_size')
    return parameters

def get_hyperparameters():
    grid_parameters = {}
    n_neighbors = st.text_input('n_neighbours')
    grid_parameters['estimator__n_neigbors'] = list(map(int, n_neighbors.split(';'))) if n_neighbors else []
    grid_parameters['estimator__algorithm'] = st.multiselect('algorithm', ['auto', 'ball_tree', 'kd_tree', 'brute'])
    leaf_size = st.text_input('leaf_size')
    grid_parameters['estimator__leaf_size'] = list(map(int, leaf_size.split(';'))) if leaf_size else []
    return grid_parameters


