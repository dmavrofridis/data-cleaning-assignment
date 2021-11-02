import pandas as pd
import numpy as np
from global_variables import *
from read_data import *
from write_data import *
from officer_linking import *
import reconciliation
import type_correction
import re

if __name__ == '__main__':

    connection = connect_to_db()
    dataframes = []
    # get the tables using the list
    for file_name in fileNames:
        df = pd.read_sql('SELECT * FROM ' + file_name, connection)
        df.name = file_name
        dataframes.append(df)

    # loop through the collected dataframes (tables) in order to perform the necessary steps
    for df in dataframes:
        print(df.name)
        # Checkpoint 2.1 (Type Correction)
        for int_column in convert_to_int:
            df = type_correction.column_to_int(df, int_column)
        for bool_column in convert_to_bool:
            df = type_correction.column_to_bool(df, bool_column)
        for date_column in convert_to_date:
            df = type_correction.column_to_date_time(df, date_column)
        for time_stamp_column in convert_to_time_stamp:
            df = type_correction.column_to_date_time(df, time_stamp_column)

        # Checkpoint 2.2 (Reconciliation)
        for string_column in reconciliation_to_string:
            df = reconciliation.column_to_proper_case(df, string_column)
        for int_column in reconciliation_to_int:
            df = reconciliation.int_correction(df, int_column)
        for date_column in reconciliation_to_date:
            df = reconciliation.date_correction(df, date_column)

    # Checkpoint 3, 3.1: Data Integration (Linking the Officers)
    # First step is to import the required tables
    data_officer = pd.read_sql('SELECT * FROM ' + "data_officer", connection)
    data_officer.name = "data_officer"
    # Populate officer_id column in trr_trr_refresh and trr_trrstatus_refresh
    # Get the instances of the two dataframes
    trr_trr_refresh = pd.read_sql('SELECT * FROM ' + "trr_trr_refresh", connection)
    trr_trr_refresh.name = "trr_trr_refresh"
    trr_trrstatus_refresh = pd.read_sql('SELECT * FROM ' + "trr_trrstatus_refresh", connection)
    trr_trrstatus_refresh.name = "trr_trrstatus_refresh"

    # Iterate through each one of the columns, find the matching values
    # if all 8 values match, then we add the officer ID to both tables
    # if not we must implement the leave one out strategy
    for column in match_columns_org:
        trr_trr_refresh[column] = data_officer[column]
        trr_trrstatus_refresh[column] = data_officer[column]

    trr_trr_refresh = officer_id_finder(trr_trr_refresh, data_officer)
    trr_trrstatus_refresh = officer_id_finder(trr_trrstatus_refresh, data_officer)



    for df in dataframes:

        # Export all the files to CSV
        write_df_to_csv(df)
