from column_processing import *
from read_data import *
from write_data import *
from officer_linking import *
import reconciliation
import type_correction

if __name__ == '__main__':

    connection = connect_to_db()
    dataframes = []
    dataframe_names = []

    # First step is to import the required tables
    data_officer = pd.read_sql('SELECT*FROM data_officer', connection)
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

        # Checkpoint 3.1
        if dataframe_names[i] == "trr_trr_refresh" or dataframe_names[i] == "trr_trrstatus_refresh":
            # Checkpoint 3.1: Data Integration (Linking the Officers)
            # Run this code to perform a left join between the dataframe and the data officer
            dataframes[i] = left_join(dataframes[i], dataframe_names[i], data_officer)

        # Checkpoint 3.2
        if dataframe_names[i] == "trr_trr_refresh":
            dataframes[i] = get_id_from_police_unit(dataframes[i], connection)

        # Checkpoint 3.3
        if dataframe_names[i] != "trr_trr_refresh":
            # print(type((dataframes[i]['trr_report_id'][2])))
            checking_for_the_final(dataframes[i], dataframes[0])

        # Checkpoint 4
        # drop the first column from charge table
        if dataframe_names[i] == "trr_charge_refresh":
            dataframes[i] = dataframes[i].drop("trr_rd_no", axis=1)
        # first rename the columns according the project guidelines
        if dataframe_names[i] == "trr_trr_refresh":
            rename_trr(dataframes[i], trr_column_proper, trr_column_mismatch)

        if dataframe_names[i] == "trr_trrstatus_refresh":
            rename_trr(dataframes[i], trr_status_column_proper, trr_status_column_mismatch)

        if dataframe_names[i] != "trr_trr_refresh":
            dataframes[i].rename(columns={"trr_report_id": "trr_id"}, inplace=True)
        # Reorder the columns
        dataframes[i] = dataframes[i][final_columns[i]]
        # Export all the files to CSV
        write_df_to_csv(dataframes[i], final_file_names[i])

'''
# Code we used during the office hours to check the validity of the table merging 
 if dataframe_names[i] == "trr_trr_refresh":
            mask = dataframes[i]["officer_birth_year"].isnull() & dataframes[i]["officer_middle_initial"].isnull()
            print(dataframes[i][mask].columns)
            list_temp = dataframes[i][mask].columns
            columns_todrop = []
            for column in list_temp:
                if column not in columns_to_drop:
                    if column in dataframes[i][mask].columns:
                        columns_todrop.append(column)

            dataframes[i] = dataframes[i].drop(columns_todrop, axis=1)
            dataframes[i] = dataframes[i].drop_duplicates(["officer_first_name", "officer_last_name"], keep='first')

            mask = dataframes[i]["officer_birth_year"].isnull() & dataframes[i]["officer_middle_initial"].isnull()

            write_df_to_csv(dataframes[i][mask], "mask")
            exit(0)

'''
