import pytest
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics


# TODO: add necessary import <DONNE>

# TODO: implement the first test. Change the function name and input as needed <DONE>
def test_data_shape_check():
    """
    This test the shape of the data to make sure it is not empty
    """
    dataframe = pd.read_csv(os.path.join(os.getcwd(), "data", "census.csv"))
    
    assert dataframe.shape[0] > 0, "Dataset has no rows"
    assert dataframe.shape[1] > 0, "Dataset has no columns"
    

# TODO: implement the second test. Change the function name and input as needed <DONE>
def test_train_model_rfc_check():
    """
    Test that train_model returns a RandomForestClassifier instance.
    """
    # Load dummy data for testing
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 2, 100)
    
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier instance"


# TODO: implement the third test. Change the function name and input as needed <DONE>
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns values between 0 and 1.
    """
    y_true = [0, 1, 1, 0, 1]
    y_pred = [0, 1, 1, 0, 0]

    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    # Assert that precision, recall, and F1-score are between 0 and 1
    assert 0 <= precision <= 1, "Precision should be between 0 and 1"
    assert 0 <= recall <= 1, "Recall should be between 0 and 1"
    assert 0 <= f1 <= 1, "F1 score should be between 0 and 1"