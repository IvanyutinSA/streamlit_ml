from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier

def get_estimator(model):
    models = {
        'KNeighborsRegressor': KNeighborsRegressor(),
        'KNeighborsClassifier': KNeighborsClassifier(),
    }
    return models[model]

def fit(estimator, X, y, target_type, grid_params):
    metric = {'Real': 'r2', 'Categorical': 'accuracy'}
    grid_params = {key: val for key, val in grid_params.items() if len(val) > 0}
    estimator = Pipeline([('estimator', estimator)])
    estimator = GridSearchCV(estimator, grid_params, cv=5, scoring=metric[target_type])
    estimator.fit(X, y)
    return estimator

def predict(estimator, X):
    return estimator.predict(X)

