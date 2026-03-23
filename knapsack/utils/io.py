"""
knapsack.utils.io
-----------------
Save and load model artifacts and data files.
"""
import joblib
from pathlib import Path


def save_model(model, path: str | Path) -> None:
    """Save a sklearn-compatible model with joblib."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"Model saved to {path}")


def load_model(path: str | Path):
    """Load a joblib-saved model."""
    return joblib.load(path)
