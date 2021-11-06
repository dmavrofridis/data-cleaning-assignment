# Data Cleaning

## Before you run the code:
- Please make sure you have an active internet connection.
- Install all the required packages.

## Instructions:
The only thing you need to do is run main from "main.py". The program will automatically perform all the necessary calculations. Upon completion, the required csv files will be generated in the output directory.


## Files:
### main.py
- Main file of the project, the one you need to run. 
- All the following files are helper files that contain functions which are called from main.

### read_data.py 
- Retrieves the necessary tables from the CPDP database (using Psycopg2).

### write_data.py 
- Outputs the CSVs into the output directory.

### column_processing.py 
- Helper file with helper functions that rename dataframe columns.

### officer_linking.py
- Generates officer ids, unit ids, and unit detail ids and checks the trr ids of other tables.

### reconciliation.py 
- Reconciles the various improperly filed data.

### type_correction.py 
- Converts data to the proper data types.

### global_variables.py 
- Contains various lists and variables used throughout the project.

## Required Packages:
#### Please make sure to install these packages, else the code might fail to run.
- Pandas
- Re
- Psycopg2
- Numpy

