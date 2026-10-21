
import numpy as np

def convert_to_dense(X):
    if hasattr(X, "toarray"):
        return X.toarray()
    return np.asarray(X)
