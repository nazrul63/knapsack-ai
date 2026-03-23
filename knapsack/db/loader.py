"""
knapsack.db.loader
------------------
Functions to load KNApSAcK DB exports into pandas DataFrames.
Supports CSV, TSV, and SQLite formats.
"""
import pandas as pd
from pathlib import Path


def load_core_db(path: str | Path) -> pd.DataFrame:
    """Load KNApSAcK Core DB. Returns DataFrame with C_ID as index."""
    raise NotImplementedError("Implement once DB format is confirmed.")


def load_activity_db(path: str | Path) -> pd.DataFrame:
    """Load KNApSAcK Activity DB."""
    raise NotImplementedError("Implement once DB format is confirmed.")


def join_activity_core(activity_df: pd.DataFrame, core_df: pd.DataFrame) -> pd.DataFrame:
    """
    Join Activity DB with Core DB on C_ID.
    Returns merged DataFrame with SMILES attached to each activity record.
    Rows without a matching SMILES are dropped with a warning.
    """
    raise NotImplementedError
