"""
knapsack.chem.pubchem
---------------------
Fallback SMILES lookup via PubChem API using InChIKey or CAS number.
Used when a compound has no SMILES in KNApSAcK Core DB.
"""
import requests
import time

PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"


def smiles_from_inchikey(inchikey: str, delay: float = 0.2) -> str | None:
    """Fetch canonical SMILES from PubChem given an InChIKey."""
    url = f"{PUBCHEM_BASE}/compound/inchikey/{inchikey}/property/CanonicalSMILES/JSON"
    try:
        time.sleep(delay)  # be polite to PubChem API
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()["PropertyTable"]["Properties"][0]["CanonicalSMILES"]
    except Exception:
        return None
