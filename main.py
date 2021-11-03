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
    dataframe_names = []

    # First step is to import the required tables
    data_officer = pd.read_sql('SELECT * FROM ' + "data_officer", connection)
    data_officer.name = "data_officer"

    # get the tables using the list
    for file_name in fileNames:
        df = pd.read_sql('SELECT * FROM ' + file_name, connection)
        dataframes.append(df)
        dataframe_names.append(file_name)

    # loop through the collected dataframes (tables) in order to perform the necessary steps
    for i in range(len(dataframes)):
        print(dataframe_names[i])
        # Checkpoint 2.1 (Type Correction)
        for int_column in convert_to_int:
            dataframes[i] = type_correction.column_to_int(dataframes[i], int_column)
        for bool_column in convert_to_bool:
            dataframes[i] = type_correction.column_to_bool(dataframes[i], bool_column)
        for date_column in convert_to_date:
            dataframes[i] = type_correction.column_to_date_time(dataframes[i], date_column)
        for time_stamp_column in convert_to_time_stamp:
            dataframes[i] = type_correction.column_to_date_time(dataframes[i], time_stamp_column)

        # Checkpoint 2.2 (Reconciliation)
        for string_column in reconciliation_to_string:
            dataframes[i] = reconciliation.column_to_proper_case(dataframes[i], string_column)
        for int_column in reconciliation_to_int:
            dataframes[i] = reconciliation.int_correction(dataframes[i], int_column)
        for date_column in reconciliation_to_date:
            dataframes[i] = reconciliation.date_correction(dataframes[i], date_column)

        # Checkpoint 3, 3.1: Data Integration (Linking the Officers)
        if dataframe_names[i] == "trr_trr_refresh" or dataframe_names[i] == "trr_trrstatus_refresh":
            # Run this code to perform a left join between the dataframe and the data officer
            dataframes[i] = left_join(dataframes[i], data_officer)

        # Export all the files to CSV
        write_df_to_csv(dataframes[i], dataframe_names[i])


