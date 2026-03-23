"""
knapsack.utils.config
---------------------
Loads per-project config.yaml into a plain dict.
"""
import yaml
from pathlib import Path


def load_config(project_name: str, base_dir: str | Path | None = None) -> dict:
    """
    Load config.yaml for a given project.

    Parameters
    ----------
    project_name : str
        Name of the project folder under projects/.
    base_dir : path, optional
        Repo root. Defaults to two levels above this file.

    Returns
    -------
    dict of config values
    """
    if base_dir is None:
        base_dir = Path(__file__).resolve().parents[2]
    config_path = Path(base_dir) / "projects" / project_name / "config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"No config.yaml found at {config_path}")
    with open(config_path) as f:
        return yaml.safe_load(f)
