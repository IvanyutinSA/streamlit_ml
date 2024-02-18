import pandas as pd
import streamlit as st
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    r2_score, mean_squared_error, mean_absolute_error,
    f1_score, accuracy_score, precision_score, log_loss,
    roc_auc_score, confusion_matrix, classification_report,
)

def get_metrics(target_type):
    metrics = {
        'Real': ['r2', 'mse', 'mae'],
        'Categorical': [
            'f1', 'accuracy', 'precision', 'log_loss', 'ROC AUC',
            'Confusion Matrix', 'classification report'
        ],
    }
    return st.multiselect('Choose', metrics[target_type])


def display_metrics(y_true, y_pred, metrics):
    functions = {
            'r2': r2_score,
            'mse': mean_squared_error,
            'mae': mean_absolute_error,
            'f1': f1_score,
            'accuracy': accuracy_score,
            'precision': precision_score,
            'log_loss': log_loss,
            'ROC AUC': roc_auc_score,
            'Confusion Matrix': confusion_matrix,
            'classification report': classification_report,
            }

    df_metrics = pd.DataFrame()
    metric_names = []
    metric_values = []

    for metric in metrics:
        if metric == 'classification report':
            st.title('Classification Report')
            st.dataframe(
                classification_report(y_true, y_pred, output_dict=True)
            )
        else:
            metric_names.append(metric)
            metric_values.append(
                functions.get(metric, wrong_metric)(y_true, y_pred)
            )
    df_metrics['Metric'] = metric_names
    df_metrics['Value'] = metric_values
    st.title('Metrics')
    st.dataframe(df_metrics)
    save_metrics(df_metrics)


def wrong_metric(**params):
    return '...'


def display_params(estimator: GridSearchCV):
    df = pd.DataFrame(
        estimator.best_params_.items(),
        columns=['Hyperparameter', 'Value']
    )
    save_params(df)
    st.title('Best model parameters')
    st.dataframe(df)


def save_params(df: pd.DataFrame):
    pass
    df.to_csv('streamlit_ml/report/best_parameters')


def save_metrics(df: pd.DataFrame):
    df.to_csv('streamlit_ml/report/metrics')
