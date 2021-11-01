import pandas as pd
from global_variables import *
from read_data import *
from write_data import *
import type_correction
import re

if __name__ == '__main__':

    # name = " O JOHN DAUCE SR"
    # last_name_and_suffix = name.split()
    # last_name = ""
    # suffix = ""
    # for element in last_name_and_suffix:
    #     if element in suffix_values:
    #         suffix = element
    #     else:
    #         if last_name == "":
    #             last_name = last_name + element
    #         else:
    #             last_name = last_name + " " + element
    #
    # print(last_name)
    # print(suffix)
    # exit(0)

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
        if df.name == 'trr_trr_refresh':
            df['officer_appointed_date'] = type_correction.clean_officer_appointed_date(df)
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
        for string_column in reconciliation_to_string:
            df = type_correction.column_to_proper_case(df, string_column)
        for int_column in reconciliation_to_int:
            df = type_correction.column_to_int(df, int_column)
        for date_column in reconciliation_to_date:
            df = type_correction.column_to_date(df, date_column)

        # Export all the files to CSV
        write_df_to_csv(df)









