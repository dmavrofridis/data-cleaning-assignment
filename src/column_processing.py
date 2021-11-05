import pandas as pd


def rename_trr(df, proper, mismatched):
    for i in range(len(proper)):
        #print(mismatched[i], proper[i])
        df.rename(columns={mismatched[i] :  proper[i]}, inplace=True)
    return df
