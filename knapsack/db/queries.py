"""
knapsack.db.queries
-------------------
Reusable query functions across all projects.
"""
import pandas as pd


def get_compounds_by_activity(df: pd.DataFrame, activity_type: str) -> pd.DataFrame:
    """Filter activity DB records by a given activity type label."""
    raise NotImplementedError


def get_compounds_by_species(df: pd.DataFrame, species_name: str) -> pd.DataFrame:
    """Filter Core DB by plant species name."""
    raise NotImplementedError
