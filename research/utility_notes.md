# Utility Electricity Research Notes

For the utility electricity source, I researched real electricity bill layouts and used that structure to create a realistic utility CSV sample.

Real electricity bills usually include customer/account number, meter number, bill date, billing period, previous meter reading, current meter reading, billed consumption in kWh, sanctioned or connected load, tariff category, fixed charges, energy charges, taxes, total bill amount, currency, and due date.

I chose to model utility ingestion as a CSV export instead of direct PDF parsing. This decision was made because utility bill PDFs vary a lot between providers, cities, and countries. For a 4-day prototype, PDF extraction would become a separate document-processing problem. A utility portal CSV export is more reliable, easier to test, and still realistic because facilities teams often download structured electricity usage reports from utility portals.

Final utility sample file:

`sample_data/utility_raw/utility_electricity_sample.csv`

The utility sample contains 20 data rows and includes these fields:

- customer_account
- meter_number
- site_code
- bill_date
- billing_period_start
- billing_period_end
- previous_reading
- current_reading
- consumption_kwh
- sanctioned_load_kw
- connected_load_kw
- tariff_category
- fixed_charges
- energy_charges
- tax_amount
- total_amount
- currency
- due_date

I included different tariff categories such as Domestic Residential, Commercial LT, Industrial HT, and Industrial. This is important because electricity data is not just a simple kWh value. Real bills also include tariff categories, demand/load details, and multiple charge components.

The sample also contains intentional data quality cases:

- one row has missing `consumption_kwh`
- one row has zero consumption but non-zero charges
- one row has negative consumption
- one row has a missing meter number
- some rows have longer billing periods
- some rows use EUR instead of INR

These cases help test the review dashboard because analysts should be able to see which rows are clean, which rows failed validation, and which rows look suspicious.

For ESG mapping, purchased electricity is mapped to Scope 2. The main activity value is `consumption_kwh`, and the normalized unit is kWh.

This utility file is meant to represent an electricity bill or portal export that a facilities team could upload during client onboarding.