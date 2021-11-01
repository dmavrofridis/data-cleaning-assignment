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



def clean_officer_appointed_date(df):
    cleaned_dates = []
    for i in range(len(df['officer_appointed_date'])):
        if 'OCT' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('OCT', '10')
            cleaned_dates.append(t)
        elif 'SEP' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('SEP', '09')
            cleaned_dates.append(t)

        elif 'AUG' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('AUG', '08')
            cleaned_dates.append(t)
        elif 'JUL' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('JUL', '07')
            cleaned_dates.append(t)
        elif 'JUN' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('JUN', '06')
            cleaned_dates.append(t)



        elif 'MAY' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('MAY', '05')
            cleaned_dates.append(t)
        elif 'APR' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('APR', '04')
            cleaned_dates.append(t)
        elif 'MAR' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('MAR', '03')
            cleaned_dates.append(t)
        elif 'FEB' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('FEB', '02')
            cleaned_dates.append(t)
        elif 'JAN' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('JAN', '01')
            cleaned_dates.append(t)

        elif 'DEC' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('DEC', '12')
            t = cleaned_dates.append(t)
        elif 'NOV' in df['officer_appointed_date'][i]:
            t = df['officer_appointed_date'][i].replace('NOV', '11')
            cleaned_dates.append(t)
        else:
            t= df['officer_appointed_date'][i]
            t = t[-2:]+'-' + t[:-3]
            if t[0] =='R' or t[0]=='E':
                del t
            elif t[:2] =='0-':
                t = '0' +t
                print(t)
                cleaned_dates.append(t)
            elif t[:2] == '1-':
                t = t[0]+'0'+ t[2:]
                cleaned_dates.append(t)
            elif int(t[:2]) >0 and int(t[:2]) <20:
                t = '20' +t
                cleaned_dates.append(t)
            else:
                t = '19' +t
                cleaned_dates.append(t)

    fin = pd.DataFrame(cleaned_dates)
    return fin


def column_to_proper_case(df, column):
    if column in df:

        if column == "officer_last_name":
            # officer_last_name - you may need to separate the last name from its suffix.
            # Remove the suffix from the last name if it exists and create new column to store the suffix
            suffix_list = []
            last_names = []

            officer_last_name_list = df['officer_last_name'].tolist()
            for last_name in officer_last_name_list:
                true_last_name = ""
                suffixed = False
                last_name_and_suffix = last_name.split()

                for element in last_name_and_suffix:
                    if element in suffix_values:
                        suffix_list.append(element)
                        suffixed = True
                    else:
                        if true_last_name == "":
                            true_last_name = true_last_name + element
                        else:
                            true_last_name = true_last_name + " " + element
                last_names.append(true_last_name)
                if not suffixed:
                    suffix_list.append("")
                # last name is going to be the first element and then second is going to be the suffix
                # last_name_and_suffix = re.split(' I | II | III | IV | V | JR | SR ', last_name)
                # if len(last_name_and_suffix) == 1:
                #     last_name_and_suffix.append(" ")
                # last_names.append(last_name_and_suffix[0])
                # suffix_list.append(last_name_and_suffix[1])
            # print(suffix_list)
            df["officer_last_name"] = last_names
            df["officer_suffix"] = suffix_list

            # Only allow applicable suffix for the new columns
            # for suffix in suffix_list:
            #     df.loc[df["officer_suffix"] != suffix, "officer_suffix"] = ""

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
