# Data Sources Summary

## SAP

I used a public SAP-style Kaggle dataset named "SAP DATASET | BigQuery Dataset". From this dataset, I focused on procurement-related tables. The main files used were `ekpo.csv` for purchase order item data and `ekko.csv` for purchase order header data.

The processed SAP file contains 100 rows and is saved as:

`sample_data/processed/sap_procurement_sample.csv`

This source was selected because SAP procurement exports are relevant to fuel and procurement activity data. Item-level purchase order data is useful for ESG ingestion because it contains material descriptions, material codes, quantities, units of measure, plant codes, values, vendor IDs, and currencies.

## Utility Electricity

For utility electricity, I created a realistic synthetic CSV based on real electricity bill structures. The sample includes meter number, customer account, billing period, previous and current readings, consumption in kWh, load values, tariff category, fixed charges, energy charges, taxes, total amount, and due date.

The utility file contains 20 rows and is saved as:

`sample_data/utility_raw/utility_electricity_sample.csv`

This source was modeled as a portal CSV export instead of PDF extraction because utility bill PDFs vary heavily across providers.

## Corporate Travel

For corporate travel, I used the public Kaggle dataset "Travel Dataset - Datathon 2019". The raw files used were `flights.csv`, `hotels.csv`, and `users.csv`.

The processed travel file contains 100 rows and is saved as:

`sample_data/processed/travel_business_sample.csv`

The processed file combines flights and hotels into one business travel format. Flights are distance-based, while hotel stays are night-based. Both are mapped to Scope 3 business travel.