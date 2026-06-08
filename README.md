# MSAT Biologics: Automated Batch Data Processing & Standardization

## 📌 Context & Problem Statement
In Biologics manufacturing (MSAT), critical process parameters (CPPs) such as cell viability, pH, dissolved oxygen, and metabolite concentrations are tracked daily. However, data often comes from disparate sources (manual lab logs, bioreactor exports, and LIMS systems) in heterogeneous formats (CSV, Excel). 

Manually aggregating and cleaning this data for analysis is time-consuming, error-prone, and poses risks to **Data Integrity**.

## 💡 The Solution: Python-Based Automation
This project demonstrates a lightweight, automated data pipeline developed in **Python** to extract, clean, and standardize multi-source bioreactor batch records into a single, analysis-ready master dataset.

### Key Features:
* **Automated Data Ingestion:** Automatically reads and merges multiple Excel/CSV files from cell culture runs.
* **Smart Data Cleaning:** Detects missing entries, handles duplicates, and flags outliers without altering raw source data.
* **Standardized Templates:** Outputs a clean, structured data format ready for immediate statistical process control (SPC) or dashboard visualization (Power BI).

## 🛡️ The Pharma Quality (QA) Edge (Data Integrity & GxP)
As a Bioengineer with 5 years of experience in Pharmaceutical Quality Assurance, this pipeline was built with **ALCOA+ principles** at its core:
* **Traceability:** Every data transformation step is fully logged with automated execution timestamps (No silent data alterations).
* **Originality & Accuracy:** Raw manufacturing data remains strictly untouched; the script strictly operates on copies to preserve the original GxP source.
* **Validation Ready:** The code structure follows clean-code principles, making it easily reviewable and auditable for computerized system validation (CSV).

## 📊 Technical Stack
* **Language:** Python
* **Libraries used (Conceptual):** `pandas` (data manipulation), `numpy` (numerical calculations), `os` (file system automation).
* **Target Users:** MSAT Scientists, Process Engineers, and Quality Officers.

