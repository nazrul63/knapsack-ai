# KNApSAcK Data Dictionary

> Maintained by the biology co-researcher. CS team uses this as the
> authoritative reference for all DB joins and feature engineering.

## Core DB

| Column | Type | Description |
|---|---|---|
| C_ID | string | Compound ID (primary key, format: C000XXXXX) |
| Name | string | Compound common name |
| SMILES | string | Canonical SMILES string |
| InChIKey | string | IUPAC InChIKey identifier |
| Molecular_Formula | string | e.g., C15H12O5 |
| Molecular_Weight | float | g/mol |
| KNApSAcK_ID | string | Internal KNApSAcK identifier |

## Activity DB

| Column | Type | Description |
|---|---|---|
| A_ID | string | Activity record ID |
| C_ID | string | Foreign key → Core DB |
| Activity | string | Raw activity label (e.g., "insecticidal") |
| Target_Organism | string | Pest or pathogen name |
| Reference | string | Literature citation |

## Structure DB

| Column | Type | Description |
|---|---|---|
| C_ID | string | Foreign key → Core DB |
| 3D_Structure | string | SDF or MOL block |
| Conformer_Source | string | Method used for 3D generation |

## KAMPO/JAMU DB

| Column | Type | Description |
|---|---|---|
| Formula_ID | string | Traditional formula ID |
| Formula_Name_JP | string | Japanese name |
| Formula_Name_EN | string | English transliteration |
| C_ID | string | Foreign key → Core DB (component compound) |
| Role | string | Primary / secondary herb role |

## WorldMap DB

| Column | Type | Description |
|---|---|---|
| Species_ID | string | Plant species ID |
| Country | string | Country of origin |
| Region | string | Geographic region |
| C_ID | string | Foreign key → Core DB |

## Join Keys

The central join is always via **C_ID** (Core DB compound ID).
All other databases foreign-key into Core DB through C_ID.

```
Core DB (C_ID)
    ├── Activity DB  (C_ID)
    ├── Structure DB (C_ID)
    ├── KAMPO DB     (C_ID)
    └── WorldMap DB  (C_ID)
```
