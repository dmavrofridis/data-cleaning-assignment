
def write_df_to_csv(df):
    path_for_csv = "./" + df.name + ".csv"
    df.to_csv(path_for_csv, index=False, header=True)