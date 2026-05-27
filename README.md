# Breathe ESG 

This repository contains the project structure and implementation for the Breathe ESG tech intern assignment.

## Project Structure

- `backend/`: Backend application source code and APIs.
- `frontend/`: Frontend web application.
- `sample_data/`: Input datasets and processed results.
  - `sap_raw/`: Raw SAP data.
  - `utility_raw/`: Raw utility consumption records.
  - `travel_raw/`: Raw business travel data.
  - `processed/`: Processed emission datasets.
- `docs/`: Technical design and decision documents.
  - `MODEL.md`: Data models and schemas.
  - `DECISIONS.md`: Design and architecture decisions.
  - `TRADEOFFS.md`: Trade-offs and analysis.
  - `SOURCES.md`: Data sources, reference constants, and emissions factor standards.
- `research/`: Domain research notes.
  - `sap_notes.md`: Research regarding SAP enterprise data.
  - `utility_notes.md`: Research regarding utility consumption calculations.
  - `travel_notes.md`: Research regarding travel emission factors.

## Data Setup

This repository contains sample files for validation, but raw large datasets are excluded from Git:
- **SAP Raw Data**: The full SAP raw dataset (`sample_data/sap_raw/`) is not committed due to its large size. It was sourced from the Kaggle dataset [mustafakeser4/sap-dataset-bigquery-dataset](https://www.kaggle.com/datasets/mustafakeser4/sap-dataset-bigquery-dataset).
- **Processed SAP Data**: A processed procurement sample (`sample_data/processed/sap_procurement_sample.csv`) and selected files (`sample_data/sap_selected/`) are committed for ease of testing.
- **Travel Data**: Business travel data is sourced from the Kaggle dataset [leomauro/argodatathon2019](https://www.kaggle.com/datasets/leomauro/argodatathon2019). The sample files (`flights.csv`, `hotels.csv`, and `users.csv`) are committed under `sample_data/travel_raw/`.
- **Utility Data**: Utility data is a realistic synthetic bill/portal export (`sample_data/utility_raw/utility_electricity_sample.csv`) modeled after researched electricity billing fields (including customer accounts, meter readings, sanctioned load, and energy tariff structures).

For instructions on how to set up the raw datasets, refer to [DATA_SETUP.md](file:///Users/alokgupta/Desktop/breathe%20esg/DATA_SETUP.md).

