# Data Setup Instructions

This document explains how to set up the raw and processed datasets required for the Breathe ESG tech intern assignment.

## Why `sample_data/sap_raw/` is Ignored

The full SAP raw dataset (`sample_data/sap_raw/`) contains enterprise-scale business tables. Due to its large size (hundreds of megabytes), committing it directly to Git slows down repository operations, exceeds recommended GitHub repository size guidelines, and contains unnecessary tables that are not used by the core prototype. 

For quick validation and testing, small selected tables and processed samples are committed to the repository under:
- `sample_data/sap_selected/`
- `sample_data/processed/`

---

## Setting Up Raw Data

If you need to reproduce the processing pipeline or work with the complete raw SAP dataset, follow these steps to download and set up the files:

### 1. Download SAP Kaggle Dataset

The raw SAP data is sourced from the Kaggle dataset:
**[mustafakeser4/sap-dataset-bigquery-dataset](https://www.kaggle.com/datasets/mustafakeser4/sap-dataset-bigquery-dataset)**

To download it using the Kaggle CLI:

1. **Install Kaggle CLI** (if not already installed):
   ```bash
   pip install kaggle
   ```

2. **Configure API Credentials**:
   - Go to your Kaggle Account page (`https://www.kaggle.com/<username>/account`).
   - Click **Create New API Token** to download `kaggle.json`.
   - Place `kaggle.json` in your home directory under `~/.kaggle/` (Linux/macOS) or `C:\Users\<username>\.kaggle\` (Windows).
   - Ensure permissions are secure (on Linux/macOS run `chmod 600 ~/.kaggle/kaggle.json`).

3. **Download and Extract Dataset**:
   Run the following commands from the project root:
   ```bash
   # Download the dataset zip
   kaggle datasets download -d mustafakeser4/sap-dataset-bigquery-dataset -p sample_data/sap_raw
   
   # Unzip the contents
   unzip sample_data/sap_raw/sap-dataset-bigquery-dataset.zip -d sample_data/sap_raw/
   
   # Clean up the downloaded zip file
   rm sample_data/sap_raw/sap-dataset-bigquery-dataset.zip
   ```

### 2. Verify File Locations

After downloading and extraction, ensure the files are in their correct paths:
- **Raw SAP Data**: All raw `.csv` tables (e.g., `ekko.csv`, `ekpo.csv`, `lfa1.csv`, `mara.csv`, `makt.csv`, `t006.csv`, `t006t.csv`) should be placed in `sample_data/sap_raw/`.
- **Selected SAP Data**: The specific raw files used to construct the processed sample are also stored in `sample_data/sap_selected/` for easy out-of-the-box usage.
- **Raw Travel Data**: Kaggle travel files (`flights.csv`, `hotels.csv`, `users.csv`) should be in `sample_data/travel_raw/`.
- **Raw Utility Data**: The electricity bill CSV should be in `sample_data/utility_raw/utility_electricity_sample.csv`.

---

## Processed Data Used by the App

The application ingests and reads from the following processed sample files:
1. **SAP Procurement Sample**: `sample_data/processed/sap_procurement_sample.csv` (contains 100 PO item rows mapped with header info).
2. **Corporate Travel Sample**: `sample_data/processed/travel_business_sample.csv` (contains 100 hotel and flight rows combined).
3. **Utility Electricity Sample**: `sample_data/utility_raw/utility_electricity_sample.csv` (contains 20 electricity bill rows).
