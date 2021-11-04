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


def left_join(df1, df1name, df2):
    append_data = []
    dropped_columns = df2.columns.values.tolist()
    dropped_columns.remove('id')
    for i in range(len(match_columns_refresh)):
        col_names = list_with_one_out(i)
        append_data.append(pd.merge(df1, df2, left_on=col_names[0], right_on=col_names[1], how='outer'))
    vertical_stack = pd.concat(append_data)

    # first, rename ids so they match the database structure
    # then, sort by officer_id (required for next step)
    # drop_duplicates, but only consider rows which ARE NOT officer_id, keep the first one (this is why sorting works,
    #   the process will naturally generate a copy of officer data that is connected to a None officer_id
    #   When we sort, Nones are pushed to the bottom.  To Keep first removes these errors
    # drop the extra row created by our process, amusingly always assigned to Karina Aaron
    if df1name == "trr_trr_refresh":
        vertical_stack = vertical_stack.rename(columns={"id_x": "id", "id_y": "officer_id"})
        vertical_stack = vertical_stack.sort_values(by='officer_id')
        vertical_stack = vertical_stack.drop_duplicates(trr_trr_refresh_cols[:-1], keep='first')
        vertical_stack = vertical_stack.dropna(subset=["id"])
    elif df1name == "trr_trrstatus_refresh":
        vertical_stack = vertical_stack.rename(columns={"id" : "officer_id"})
        vertical_stack = vertical_stack.sort_values(by='officer_id')
        vertical_stack = vertical_stack.drop_duplicates(trr_trrstatus_refresh_cols[:-1], keep='first')
        vertical_stack = vertical_stack.dropna(subset=["trr_report_id"])

    # This is a list which contains the name of the columns that we have to drop when mergin tables
    # first_name, middle_initial, last_name, suffix_name (if applicable), gender, race, appointed_date, birth year
    dropped_columns = dropped_columns + columns_to_drop
    vertical_stack = vertical_stack.drop(dropped_columns, axis=1)


    # print(dropped_columns)
    # print(vertical_stack.columns.values.tolist())


    return vertical_stack


def get_id_from_police_unit(vertical_stack, connection):
    police_unit = pd.read_sql('SELECT * FROM ' + "data_policeunit", connection)
    police_unit = police_unit[['unit_name', 'id']]
    cleaned_id = []
    for i in police_unit['unit_name']:
        if i == '000':
            cleaned_id.append(0)
        else:
            index = 0
            while i[index] == '0':
                index += 1
            cleaned_id.append(i[index:])
    police_unit['unit_name'] = pd.DataFrame(cleaned_id)
    df = pd.merge(vertical_stack, police_unit, how='left', left_on='officer_unit_name', right_on='unit_name')
    df = df.drop('unit_name', axis=1)
    df = df.rename(columns={"id_x": 'id', "id_y": "officer_unit_id"})

    return df


# Checkpoint 3.3
def checking_for_the_final(df, trr_trr_refresh):
    trr_ids = list(trr_trr_refresh['id'])
    trr_ids = [str(i) for i in trr_ids]
    new_df = pd.DataFrame(columns=df.columns)
    for ind in range(len(df['trr_report_id'])):
        try:
            temp = df['trr_report_id'][ind]
            if str(temp) in trr_ids:
                try:
                    #print('there')
                    new_df.append(df[ind:ind+1])
                except:
                    continue
            else:
                print('remove')
        except:
            continue






