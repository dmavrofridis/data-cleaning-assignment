import pandas as pd
from global_variables import *
from read_data import *
from write_data import *
import type_correction

if __name__ == '__main__':

    fileNames = ["trr_trr_refresh", "trr_actionresponse_refresh", "trr_charge_refresh",
                 "trr_subjectweapon_refresh", "trr_trrstatus_refresh", "trr_weapondischarge_refresh"]

    # Load the first file from the csv to pandas dataframe
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
            df = type_correction.column_to_date(df, date_column)
        for time_stamp_column in convert_to_time_stamp:
            df = type_correction.column_to_time_stamp(df, time_stamp_column)

        # Checkpoint 2.2 (Reconciliation)

        # Export all the files to CSV
        write_df_to_csv(df)









