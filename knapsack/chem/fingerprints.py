"""
knapsack.chem.fingerprints
--------------------------
Convert SMILES strings to molecular fingerprint vectors.
Used by BioGuard, NaturalHit, AuthentiScan, and others.
"""
import numpy as np
from typing import Optional


def smiles_to_morgan(
    smiles: str,
    radius: int = 2,
    n_bits: int = 2048,
) -> Optional[np.ndarray]:
    """
    Convert a SMILES string to an ECFP4 Morgan fingerprint.

    Parameters
    ----------
    smiles : str
        Input SMILES string.
    radius : int
        Morgan algorithm radius. 2 = ECFP4 (default), 3 = ECFP6.
    n_bits : int
        Fingerprint bit vector length.

    Returns
    -------
    np.ndarray of shape (n_bits,) or None if SMILES is invalid.
    """
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=n_bits)
        return np.array(fp)
    except Exception:
        return None


def batch_smiles_to_morgan(
    smiles_list: list[str],
    radius: int = 2,
    n_bits: int = 2048,
) -> tuple[list[np.ndarray], list[int]]:
    """
    Convert a list of SMILES to Morgan fingerprints.

    Returns
    -------
    (fingerprints, failed_indices)
        fingerprints: list of np.ndarray for valid SMILES
        failed_indices: list of indices where conversion failed
    """
    fps, failed = [], []
    for i, smi in enumerate(smiles_list):
        fp = smiles_to_morgan(smi, radius=radius, n_bits=n_bits)
        if fp is not None:
            fps.append(fp)
        else:
            failed.append(i)
    return fps, failed
