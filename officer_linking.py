from global_variables import *
from global_variables import *
import pandas as pd

# Checkpoint 3.1
def list_with_one_out(index):
    list_org = []
    list_refresh = []
    for i in range(len(match_columns_refresh)):
        if i != index:
            list_org.append(match_columns_org[i])
            list_refresh.append(match_columns_refresh[i])

    return list_refresh, list_org


def left_join(df1, df2):
    append_data = []
    dropped_columns = df2.columns.values.tolist()
    dropped_columns.remove('id')
    for i in range(len(match_columns_refresh)):
        col_names = list_with_one_out(i)
        append_data.append(pd.merge(df1, df2, left_on=col_names[0], right_on=col_names[1]))
    vertical_stack = pd.concat(append_data)
    # This is a list which contains the name of the columns that we have to drop when mergin tables
    # first_name, middle_initial, last_name, suffix_name (if applicable), gender, race, appointed_date, birth year
    dropped_columns = dropped_columns + columns_to_drop
    vertical_stack = vertical_stack.drop(dropped_columns, axis=1)
    vertical_stack = vertical_stack.rename(columns={"id_x": "id", "id_y": "officer_id"})
    vertical_stack = vertical_stack.drop_duplicates()
    # print(dropped_columns)
    # print(vertical_stack.columns.values.tolist())

    return vertical_stack
