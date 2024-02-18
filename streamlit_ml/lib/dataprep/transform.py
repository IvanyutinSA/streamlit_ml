from sklearn.preprocessing import StandardScaler
from category_encoders import BinaryEncoder
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split

import numpy as np
import streamlit as st


transformers = {
    'wine': ColumnTransformer(transformers=[
        ('num', StandardScaler(), [
            'fixed acidity','volatile acidity','citric acid','residual sugar',
            'chlorides','free sulfur dioxide','total sulfur dioxide','density',
            'pH','sulphates','alcohol'
            ])
        ]),
    'airlines': ColumnTransformer(transformers=[
        ('num', StandardScaler(), [
            'Flight', 'DayOfWeek', 'Time', 'Length'
            ]),
        ('cat', BinaryEncoder(), [
            'Airline', 'AirportFrom', 'AirportTo'
            ])
        ])
}

def transform_features(X, dataset):
    d = {'airlines': ['Flight', 'DayOfWeek', 'Time', 'Length', 'Airline', 
                      'AirportFrom', 'AirportTo']}
    if dataset in d:
        X = X[d[dataset]]
    return transformers[dataset].fit_transform(X)

def get_train_test_split(df, dataset):
    X = df[df.columns[:-1]]
    y = df[df.columns[-1]]
    
    X = transform_features(X, dataset)

    return train_test_split(X, y, test_size=.2, stratify=y)

