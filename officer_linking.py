from global_variables import *


def officer_id_finder(df1, df2):
    # Now the refresh tables also contain the columns from the original table
    # Now it is time to
    for i in range(len(df1)):
        for j in range(len(df2)):
            count = 0
            for column_index in range(len(match_columns_refresh)):
                # if df1[match_columns_refresh[column_index]][i] == df2[match_columns_org[column_index]][j]:
                    count += 1
            if count >= 6:
                df1[new_columns[0]][i] = df2[match_columns_org["officer_id"]][j]
    return df1

'''
pd.merge(df1, df2, on= ['df'
'''