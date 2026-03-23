# KNApSAcK-AI

> AI-driven discovery tools built on the [KNApSAcK Family Database](http://www.knapsackfamily.com/) —
> the world's largest integrated plant metabolite database, developed at NAIST over 20+ years.

## Overview

KNApSAcK-AI is a research monorepo developing machine learning and AI tools across four industry domains:

| Domain | Projects |
|---|---|
| 🌾 Agriculture / Biopesticides | BioGuard, WhiteSpace Finder |
| 💊 Pharmaceutical / Drug Discovery | NaturalHit, NaturalDock |
| 🥗 Nutraceutical / Functional Food | IngredientLens, ClaimScore |
| 🌿 KAMPO / JAMU Traditional Medicine | AuthentiScan, SynergyMap, SourceAtlas |
| 🤖 AI Infrastructure | KNApSAcK-GPT |

## Project Status

| Project | Tier | Status | Domain |
|---|---|---|---|
| BioGuard | 1 | 🟡 In Progress | Agriculture |
| IngredientLens | 1 | 🔴 Planned | Nutraceutical |
| AuthentiScan | 1 | 🔴 Planned | KAMPO/QC |
| NaturalHit | 2 | 🔴 Planned | Pharma |
| ClaimScore | 2 | 🔴 Planned | Nutraceutical |
| WhiteSpace Finder | 2 | 🔴 Planned | Agriculture |
| NaturalDock | 3 | 🔴 Planned | Pharma |
| SynergyMap | 3 | 🔴 Planned | KAMPO |
| SourceAtlas | 3 | 🔴 Planned | ESG/Supply Chain |
| KNApSAcK-GPT | 4 | 🔴 Planned | AI Infrastructure |

## Repository Structure

```
knapsack-ai/
├── knapsack/          # Shared core library (used by all projects)
│   ├── db/            # KNApSAcK DB loaders and query functions
│   ├── chem/          # Molecular fingerprinting, SMILES utilities
│   ├── ml/            # Shared ML utilities, metrics, splitters
│   └── utils/         # Logging, config, I/O helpers
├── projects/          # One folder per product
│   ├── bioguard/
│   ├── ingredientlens/
│   └── ...
├── data/              # Raw DB exports and processed outputs (gitignored)
├── docs/              # Vision, roadmap, data dictionary
└── scripts/           # Setup and pipeline runner scripts
```

## Quick Start

```bash
# Clone
git clone https://github.com/nazrul63/knapsack-ai.git
cd knapsack-ai

# Create environment (conda recommended for RDKit)
conda env create -f environment.yml
conda activate knapsack-ai

# Install shared library in editable mode
pip install -e .

# Run a project
python scripts/run_project.py bioguard
```

## Team

- **Mohammad Imran Khan** — PhD student, Computational Systems Biology Lab, NAIST
- **A S M Nazrul Islam** — PhD student, Computational Systems Biology Lab, NAIST
- Supervisor: **Prof. Shigehiko Kanaya**, NAIST, **Assoc. Prof. Md Altaf-Ul-Amin**, NAIST, **Asst. Prof. Mohammed Kamal Nasution**, NAIST

## License

MIT License — see [LICENSE](LICENSE)
