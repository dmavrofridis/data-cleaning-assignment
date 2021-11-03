
def write_df_to_csv(df, df_name):
    path_for_csv = "./csv_files/" + df_name + ".csv"
    df.to_csv(path_for_csv, index=False, header=True)