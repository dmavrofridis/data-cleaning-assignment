import pandas as pd
from global_variables import *
import type_correction
import re


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
                updated_last_name, suffix = last_name_and_suffix(last_name)
                last_names.append(updated_last_name)
                suffix_list.append(suffix)

            df["officer_last_name"] = last_names
            df["officer_suffix"] = suffix_list

        elif column == "officer_gender":
            for male_gender_value in male_gender_values:
                df.loc[df[column] == male_gender_value, column] = reconciled_male_value
            for female_gender_value in female_gender_values:
                df.loc[df[column] == female_gender_value, column] = reconciled_female_value

        elif column == "subject_race" or "officer_race":
            column_race_correction(df, column)

        '''
        elif column == "street" or column == "location":
            df.loc["-" in df[column], column] = df[column].replace("-", " ")
            '''

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
                        df.loc[df[column] == race, column] = processed_race
                        completed = True


def last_name_and_suffix(last_name):
    last_name_suffix = last_name.split()
    last_name = ""
    suffix = ""
    for element in last_name_suffix:
        if element in suffix_values:
            suffix = element
        else:
            if last_name == "":
                last_name = last_name + element
            else:
                last_name = last_name + " " + element

    return last_name, suffix


def date_correction(df, column):
    if column in df:
        df = type_correction.column_to_date_time(df, column)
    # officer_appointed_date - if the date is in the future, i.e., after 2021, subtract 100 years.
    return df


def int_correction(df, column):
    if column in df:
        df = type_correction.column_to_int(df, column)
        if column == "subject_birth_year":
            # subject_birth_year - this one might require sanity checks, e.g., if you see a birth year of 40 then map
            # it to 1940 for years > 5 and less than 100
            df.loc[(5 < df[column]) & (df[column] < 100), column] += 1900
    return df