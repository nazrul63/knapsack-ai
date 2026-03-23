"""
knapsack.chem.standardize
-------------------------
SMILES canonicalization and molecule standardization utilities.
"""


def canonicalize_smiles(smiles: str) -> str | None:
    """Return canonical SMILES or None if invalid."""
    try:
        from rdkit import Chem
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        return Chem.MolToSmiles(mol)
    except Exception:
        return None
