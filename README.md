# CarForce Data-X Project

## Authors
* Julian Kudszus, Soham Kudtarkar, Spencer Lee, Nicholas Hirons
* Project and data courtesy of [CarForce](http://www.thecarforce.com/)

## Outline
* Predict likely service operations from error codes, time of year and car features such as make, age, mileage, engine size

## Data
Raw data is stored in ./data directory on local drive, with raw files converted to .csv:
* ./data/20170622_1514_SV (376k).csv
* ./data/SVC Aggregate (115k).csv
* ./data/all_data.csv
* ./data/error_codes_only.csv

Preprocessed data is stored in all.csv in main directory. Note:
* Raw variables to ignore: make, op_descriptions, date, appointment_month, season, year
* Target variables have a 'y_' prefix
* Input variables (all other columns) are either one hot encoded or numeric