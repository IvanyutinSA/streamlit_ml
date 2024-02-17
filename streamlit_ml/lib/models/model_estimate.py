import streamlit as st

def get_metrics(target_type):
    metrics = {
        'Real': ['r2', 'mse', 'mae', 'mapa'],
        'Categorical': [
            'f1', 'accuracy', 'precision', 'log_loss', 'ROC AUC',
            'Confusion Matrix', 'classification report'
        ],
    }
    return st.multiselect('Choose', metrics)

