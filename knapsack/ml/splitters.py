"""
knapsack.ml.splitters
---------------------
Train/val/test split strategies for all projects.
Always use stratified splits for classification tasks.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def stratified_split(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    val_size: float = 0.1,
    random_seed: int = 42,
) -> tuple:
    """
    Stratified train/val/test split.

    Returns
    -------
    (X_train, X_val, X_test, y_train, y_val, y_test)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_seed
    )
    val_ratio = val_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=val_ratio, stratify=y_train, random_state=random_seed
    )
    return X_train, X_val, X_test, y_train, y_val, y_test
