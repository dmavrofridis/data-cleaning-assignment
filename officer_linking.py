from global_variables import *

def officer_id_finder(df1, officer_table):
    officer_ids = []
    operations = 0

    for i in range(0, 10):
        operations += 1
        print(operations)
        # for loop for the columns
        for j in range(0, len(match_columns_refresh)):
            # counter for the number of columns that matched
            matching_columns = 0
            failed_columns = 0
            print("We are at line -> " + str(operations) + " and on column -> " + match_columns_refresh[j])

            # for loop for the officer_table
            for k in range(0, len(officer_table)):
                if df1[match_columns_refresh[j]][i] == officer_table[match_columns_org[j]][k]:
                    matching_columns += 1
                else:
                    failed_columns += 1

                if failed_columns > 1:
                    officer_ids.append("")
                    break
                elif matching_columns >= 7:
                    officer_ids.append(officer_table["id"][k])
                    break

    # df1[new_columns[0]] = officer_ids
    for id in officer_ids:
        print(id)
    return df1


def list_with_one_out(index):
    list_org = []
    list_refresh = []
    for i in range(len(match_columns_refresh)):
        if i != index:
            list_org.append(match_columns_org[i])
            list_refresh.append(match_columns_refresh[i])

    return list_org, list_refresh


def left_join(df1, df2):
    append_data = []
    dropped_columns = df2.columns.values.tolist()
    dropped_columns.remove('id')
    for i in range(len(match_columns_refresh)):
        col_names = list_with_one_out(i)
        append_data.append(pd.merge(df1, df2, left_on=col_names[1], right_on=col_names[0]))
    vertical_stack = pd.concat(append_data)
    vertical_stack = vertical_stack.drop(dropped_columns, axis =1)

    vertical_stack = vertical_stack.rename(columns={"id_x" : "id", "id_y" : "officer_id"})
    # print(dropped_columns)
    # print(vertical_stack.columns.values.tolist())


    return vertical_stack
