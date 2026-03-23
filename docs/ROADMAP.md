# KNApSAcK-AI — Project Roadmap

## Tier 1 — Months 1–6 (Single DB, proven methods, fast results)

| Project | DB(s) Needed | Method | Target Output |
|---|---|---|---|
| BioGuard | Activity DB + Core DB | Random Forest on ECFP4 | Pesticidal activity classifier |
| IngredientLens | Core DB + Activity DB | Text classification | FOSHU category mapper |
| AuthentiScan | Core DB | ML fingerprint matching | Species authentication tool |

## Tier 2 — Months 6–12 (Two DBs, moderate complexity)

| Project | DB(s) Needed | Method | Target Output |
|---|---|---|---|
| NaturalHit | Activity DB + Structure DB | GNN | Bioactivity predictor |
| ClaimScore | Activity DB + PubMed API | NLP evidence grading | Health claim validator |
| WhiteSpace Finder | Core DB + Activity DB + Patent API | Data pipeline | IP gap finder |

## Tier 3 — Months 12–18 (Multiple DBs, high complexity)

| Project | DB(s) Needed | Method | Target Output |
|---|---|---|---|
| NaturalDock | Structure DB + PDB | AutoDock Vina | Docking score predictor |
| SynergyMap | KAMPO DB + Core DB + Activity DB | Network analysis | Synergy mapper |
| SourceAtlas | WorldMap DB + Core DB + Climate API | GIS + scoring | Sustainable sourcing tool |

## Tier 4 — Year 2–3 (Capstone, integrates everything)

| Project | Dependencies | Method | Target Output |
|---|---|---|---|
| KNApSAcK-GPT | All above projects | RAG + Knowledge Graph | Natural language query system |

## Key Milestones

- [ ] Month 1: Repo scaffold + data audit complete
- [ ] Month 3: BioGuard baseline model (macro F1 > 0.70)
- [ ] Month 6: BioGuard paper submitted + IngredientLens prototype
- [ ] Month 12: NaturalHit GNN trained + AuthentiScan deployed
- [ ] Month 18: Tier 3 projects initiated
- [ ] Year 3: KNApSAcK-GPT integrated system + capstone paper
