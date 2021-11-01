import pandas as pd


def column_to_int(df, column):
    if column in df:
        df[column] = pd.to_numeric(df[column])
    return df


def column_to_bool(df, column):
    if column in df:
        df.loc[df[column] == "Y", column] = 1
        df.loc[df[column] == "YES", column] = 1
        df.loc[df[column] == "Yes", column] = 1
        df.loc[df[column] == "yes", column] = 1

        df.loc[df[column] == "N", column] = 0
        df.loc[df[column] == "NO", column] = 0
        df.loc[df[column] == "No", column] = 0
        df.loc[df[column] == "no", column] = 0
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
