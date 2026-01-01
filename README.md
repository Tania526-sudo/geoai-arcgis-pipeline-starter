# geoai-arcgis-pipeline-starter
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-Geospatial-2C8C4A?logo=python&logoColor=white)](#)
[![ArcGIS API for Python](https://img.shields.io/badge/ArcGIS%20API%20for%20Python-Ready-0079C1?logo=esri&logoColor=white)](#)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-34D058?logo=opensourceinitiative&logoColor=white)](#)

**Production-ready starter** for a **GeoAI → QA/QC → ArcGIS publishing** pipeline.  
This repository demonstrates how to ingest geospatial data, validate it using a repeatable QA framework, generate ML/GeoAI-ready features, and publish **GIS-ready layers** to **ArcGIS Online / ArcGIS Enterprise** with automated reporting.

> **Confidentiality note:** Some real-world implementations and datasets are private due to critical-infrastructure constraints. This repo provides a **safe demo pipeline** with open/public data and reproducible notebooks. A live demo can be shown during interviews under data confidentiality rules.

---

## What you get
- **Data ingest** (CSV/GeoJSON/Parquet/OSM extracts)  unified GeoDataFrame
- **QA/QC validation** (schema contract, geometry validity, CRS checks, near-duplicates, outliers)
- **GeoAI feature engineering** (spatial joins, distance features, density, time-ready structure)
- **ArcGIS publishing**:
  - create Hosted Feature Layer / Feature Service
  - update schema, symbology hints, metadata
  - publish web map (optional)
- **Reporting**: QA summary tables + machine-readable JSON report (CI-friendly)

---

## Quick links
- **Portfolio / Profile:** (https://www.linkedin.com/in/tetiana-starovoit-61b246200/)
- **Demo Notebook (start here):** [`notebooks/00_quickstart.ipynb`](notebooks/00_quickstart.ipynb)
- **QA/QC Notebook:** [`notebooks/02_qaqc_validation.ipynb`](notebooks/02_qaqc_validation.ipynb)
- **ArcGIS Publish Notebook:** [`notebooks/03_arcgis_publish.ipynb`](notebooks/03_arcgis_publish.ipynb)

---

## Repository structure
```text
geoai-arcgis-pipeline-starter/
├─ notebooks/
│  ├─ 00_quickstart.ipynb
│  ├─ 01_data_ingest_and_eda.ipynb
│  ├─ 02_qaqc_validation.ipynb
│  ├─ 03_arcgis_publish.ipynb
│  └─ 04_geoai_features_and_scoring.ipynb
├─ src/
│  ├─ geoai/
│  │  ├─ features.py
│  │  └─ scoring.py
│  ├─ qaqc/
│  │  ├─ contract.py
│  │  ├─ checks.py
│  │  └─ report.py
│  ├─ arcgis/
│  │  ├─ connect.py
│  │  ├─ publish.py
│  │  └─ metadata.py
│  └─ utils/
│     ├─ io.py
│     └─ logging.py
├─ data/
│  ├─ 00_raw/
│  ├─ 01_clean/
│  └─ 02_qaqc/
├─ configs/
│  ├─ pipeline.yaml
│  └─ qaqc_rules.yaml
├─ .github/workflows/
│  └─ ci.yml
├─ pyproject.toml
├─ README.md
└─ LICENSE

