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

## ⚙️ How the Pipeline Logic Works (Pseudocode)

To ensure maximum transparency and align with Computerized System Validation (CSV) expectations, the automation sequence follows these strict logical steps:

1. **Ingestion:** Scan the target directory for new production `.csv` or `.xlsx` exports.
2. **Structural Check:** Verify that required columns (`Batch_ID`, `pH`, `Viable_Cell_Density`) exist. If not, trigger a critical GxP log alert.
3. **Data Cleaning:** 
   * Forward-fill missing `Batch_ID` values based on time-series proximity.
   * Apply a data-integrity filter to isolate and remove non-physical outliers (e.g., VCD values > 100 M/mL).
   * Interpolate isolated missing sensor records (like `DO_Percent`) using rolling averages.
4. **Traceability Logging:** Generate an automated text log capturing the number of rows modified, execution time, and user ID to maintain a perfect audit trail.
5. **Export:** Write the standardized dataset into the secure `data_example_clean.csv` repository for downstream MSAT monitoring.

