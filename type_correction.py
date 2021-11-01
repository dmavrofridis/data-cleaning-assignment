import pandas as pd
from global_variables import *
import re


def column_to_int(df, column):
    if column in df:
        df[column] = pd.to_numeric(df[column])
    return df


def column_to_bool(df, column):
    if column in df:
        for yes_value in yes_values:
            df.loc[df[column] == yes_value, column] = 1
        for no_value in no_values:
            df.loc[df[column] == no_value, column] = 0
    return df


def column_to_time_stamp(df, column):
    if column in df:
        df.loc[df[column] == "REDACTED", column] = " "
        df[column] = pd.to_datetime(df[column], errors="ignore", yearfirst=True)
    return df


def column_to_date(df, column):
    if column in df:
        df.loc[df[column] == "REDACTED", column] = " "
        df[column] = pd.to_datetime(df[column], errors="ignore", yearfirst=True)
    return df


def column_to_proper_case(df, column):
    if column in df:

        if column == "officer_last_name":
            # officer_last_name - you may need to separate the last name from its suffix.
            # Remove the suffix from the last name if it exists and create new column to store the suffix
            suffix_list = []
            last_names = []
            officer_last_name_list = df['officer_last_name'].tolist()
            for last_name in officer_last_name_list:
                # last name is going to be the first element and then second is going to be the suffix
                last_name_and_suffix = re.split(' I | II | III | IV | V | JR | SR ', last_name)
                if len(last_name_and_suffix) == 1:
                    last_name_and_suffix.append(" ")
                last_names.append(last_name_and_suffix[0])
                suffix_list.append(last_name_and_suffix[1])

            df["officer_last_name"] = last_names
            df["officer_suffix"] = suffix_list

            # Only allow applicable suffix for the new columns
            for suffix in suffix_name:
                df.loc[df["officer_suffix"] != suffix, "officer_suffix"] = ""

        elif column == "officer_gender":
            for male_gender_value in male_gender_values:
                df.loc[df["officer_gender"] == male_gender_value, "officer_gender"] = reconciled_male_value
            for female_gender_value in female_gender_values:
                df.loc[df["officer_gender"] == female_gender_value, "officer_gender"] = reconciled_female_value

        elif column == "subject_race":
            column_race_correction(df, "subject_race")

        elif column == "officer_race":
            column_race_correction(df, "officer_race")

        # Finally convert the string to title ( Proper Case ) after preprocessing
        df[column] = df[column].str.upper().str.title()

    return df


def column_race_correction(df, column):
    for race in race_values:
        words = race.lower().split("/")
        completed = False
        for word in words:
            if not completed:
                for processed_race in reconciled_race_values:
                    if word in processed_race.lower():
                        print(race + " changed to ---> " + processed_race)
                        df.loc[df[column] == race, column] = processed_race
                        completed = True
