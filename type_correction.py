import pandas as pd
from global_variables import *
import re


def column_to_int(df, column):
    if column in df:
        df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0.0).astype(int)
    return df


def column_to_bool(df, column):
    if column in df:
        for yes_value in yes_values:
            df.loc[df[column] == yes_value, column] = True
        for no_value in no_values:
            df.loc[df[column] == no_value, column] = False
    return df


def column_to_date_time(df, column):
    if column in df:
        df.loc[df[column] == "REDACTED", column] = None
        # We make sure to add the optional "coerce" options when raising errors to allow pandas to turn date to correct
        # format
        df[column] = pd.to_datetime(df[column], errors='coerce')
    return df
