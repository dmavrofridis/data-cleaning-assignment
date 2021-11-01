import pandas as pd
from global_variables import *


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
            df[['officer_last_name', 'officer_suffix']] = df.officer_last_name.str.split(" ", expand=True)
            # Only allow applicable suffix for the new columns
            for suffix in suffix_name:
                df.loc[df["officer_suffix"] is not suffix, "officer_suffix"] = ""

        elif column == "officer_gender":
            for male_gender_value in male_gender_values:
                df.loc[df["officer_gender"] == male_gender_value, "officer_gender"] = reconciled_male_value
            for female_gender_value in female_gender_values:
                df.loc[df["officer_gender"] == female_gender_value, "officer_gender"] = reconciled_female_value

        # Finally convert the string to title ( Proper Case ) after preprocessing
        df[column] = df[column].str.upper().str.title()
    return df
