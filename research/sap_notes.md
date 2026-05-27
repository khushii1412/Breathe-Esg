# SAP Data Research Notes

For the SAP source, I used a public Kaggle dataset called "SAP DATASET | BigQuery Dataset". The dataset contains SAP-style replicated business tables across procurement, finance, sales, vendors, materials, units of measure, and other enterprise modules.

For this prototype, I focused only on the procurement-related tables because the assignment specifically mentions SAP fuel and procurement data. I did not use every SAP table from the dataset because that would make the prototype unnecessarily large and difficult to explain.

The main SAP files used were:

- `ekpo.csv`: Purchasing Document Item
- `ekko.csv`: Purchasing Document Header
- `ekkn.csv`: Purchase Order Account Assignment
- `lfa1.csv`: Vendor Master Data
- `mara.csv`: Material Master Data
- `makt.csv`: Material Descriptions
- `t006.csv` and `t006t.csv`: Units of Measure

For the processed SAP sample, I used `ekpo.csv` as the main file because it contains purchase order item-level data. This is the most useful level for ESG ingestion because each row represents a purchased item or material with quantity, unit, plant, material code, material description, and value.

I joined `ekpo.csv` with `ekko.csv` using the purchase order number field `ebeln`. `ekpo.csv` gives item-level details, while `ekko.csv` gives header-level details like currency, vendor ID, purchase order date, purchasing organization, and country.

Final processed SAP file:

`sample_data/processed/sap_procurement_sample.csv`

The processed SAP file contains 100 rows and includes these fields:

- purchase_order_number
- purchase_order_item
- item_changed_date
- material_description
- material_code
- company_code
- plant_code
- material_group
- quantity
- unit_of_measure
- net_price
- net_value
- gross_value
- net_weight
- weight_unit
- vendor_id
- currency
- purchase_order_date
- purchasing_org
- purchasing_group
- country

I chose this structure because it looks close to how procurement data is usually handled in SAP systems. In a real enterprise onboarding, SAP exports would usually contain internal plant codes, material codes, vendor IDs, quantities, units of measure, prices, and currencies. These fields are important because ESG analysts need to trace each activity row back to the original enterprise source.

For ESG mapping, SAP procurement rows can represent different scopes depending on the material purchased. Fuel-related purchases such as diesel, petrol, LPG, or generator fuel would be mapped to Scope 1. General purchased goods and materials would be mapped to Scope 3 purchased goods and services.

For this prototype, the SAP file mainly demonstrates procurement ingestion, source tracking, quantity/unit handling, plant-code handling, and audit traceability.