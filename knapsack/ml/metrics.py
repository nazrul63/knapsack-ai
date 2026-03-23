"""
knapsack.ml.metrics
-------------------
Shared evaluation functions used across all classification projects.
"""
import numpy as np
import pandas as pd
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    f1_score,
)


def evaluate_multiclass(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: np.ndarray | None = None,
    class_names: list[str] | None = None,
) -> dict:
    """
    Compute standard multiclass classification metrics.

    Returns a dict with:
        - per_class_f1
        - macro_f1
        - weighted_f1
        - classification_report (string)
        - confusion_matrix (np.ndarray)
        - roc_auc (if y_prob provided)
    """
    result = {
        "macro_f1": f1_score(y_true, y_pred, average="macro"),
        "weighted_f1": f1_score(y_true, y_pred, average="weighted"),
        "per_class_f1": f1_score(y_true, y_pred, average=None).tolist(),
        "classification_report": classification_report(
            y_true, y_pred, target_names=class_names
        ),
        "confusion_matrix": confusion_matrix(y_true, y_pred),
    }
    if y_prob is not None:
        try:
            result["roc_auc"] = roc_auc_score(
                y_true, y_prob, multi_class="ovr", average="macro"
            )
        except ValueError:
            result["roc_auc"] = None
    return result
