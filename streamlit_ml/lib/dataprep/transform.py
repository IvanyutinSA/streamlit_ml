from streamlit_ml.app.dashboard import dataset

from sklearn.preprocessing import StandardScaler
from category_encoders import BinaryEncoder
from sklearn.compose import ColumnTransformer


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

def tranform_features(X):
    return transformers[dataset].fit_transform(X)

