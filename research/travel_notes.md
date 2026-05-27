# Corporate Travel Research Notes

For the corporate travel source, I first looked at Concur-style travel data, but public Concur client exports are not easily available because they usually contain private employee and booking information.

Instead, I used a public Kaggle dataset called "Travel Dataset - Datathon 2019". This dataset contains travel-related files for flights, hotels, and users. It is not a Concur export, but it is a suitable public travel dataset for building a realistic business travel ingestion prototype.

The raw travel files downloaded were:

- `flights.csv`
- `hotels.csv`
- `users.csv`

The flight file includes fields such as travel code, user code, origin, destination, flight type, price, time, distance, agency, and date. The hotel file includes travel code, user code, hotel name, place, days, price, total, and date. The users file includes user code, company, name, gender, and age.

For the processed travel sample, I created one combined business travel file from flights and hotels.

Final processed travel file:

`sample_data/processed/travel_business_sample.csv`

The processed travel file contains 100 rows and includes these fields:

- expense_report_id
- employee_id
- travel_date
- category
- origin
- destination
- distance_km
- cabin_class
- hotel_nights
- amount
- currency
- vendor

I converted flight rows into a standard format where the category is `Flight`, the origin and destination come from the flight route, the distance is stored in kilometers, the cabin class comes from the flight type, and the vendor comes from the travel agency.

I converted hotel rows into the same standard format where the category is `Hotel`, the origin and destination are both the hotel location, hotel nights come from the number of days, and the vendor is the hotel name.

This structure is useful because corporate travel data often contains different activity types in different shapes. Flights are distance-based, while hotels are night-based. A single normalized format lets the system handle both sources in one review dashboard.

For ESG mapping, corporate travel is mapped to Scope 3 business travel. Flight rows are treated as Scope 3 business travel flights, and hotel rows are treated as Scope 3 business travel hotel stays.

The current travel sample does not include ground transport because the public dataset only provides flights and hotels. In a real deployment, ground transport would be added from expense categories such as taxi, ride-share, rental car, or mileage reimbursement.