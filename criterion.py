import numpy as np
from sklearn.metrics import mean_squared_error


class MSE():
    def __init__(self):
        pass

    def __call__(self, X, X_l, X_r, y, y_l, y_r):
        return self._calc(X, y) - self._calc(X_l, y_l) - self._calc(X_r, y_r)

    def _calc(self, X, y):
        return np.sum(np.power(y - np.mean(y), 2))


class MSE_by_model():
    def __init__(self, model):
        self.model = model

    def __call__(self, X, X_l, X_r, y, y_l, y_r):
        return self._calc(X, y) - self._calc(X_l, y_l) - self._calc(X_r, y_r)

    def _calc(self, X, y):
        self.model.fit(X, y)
        return mean_squared_error(y, self.model.predict(X))
