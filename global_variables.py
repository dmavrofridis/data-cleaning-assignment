conn_string = "host='codd01.research.northwestern.edu' dbname='postgres' user='cpdbstudent' password='DataSci4AI'"

fileNames = ["trr_trr_refresh", "trr_actionresponse_refresh", "trr_charge_refresh",
             "trr_subjectweapon_refresh", "trr_trrstatus_refresh", "trr_weapondischarge_refresh"]

'''Variables for Checkpoint 2.1 (Data Cleaning)'''
convert_to_int = ["beat", "officer_birth_year", "officer_age", "subject_birth_year", "subject_age",
                  "officer_birth_year"]
convert_to_bool = ["officer_on_duty", "officer_injured", "officer_in_uniform", "subject_armed",
                   "subject_injured", "subject_alleged_injury", "notify_oemc", "notify_district_sergeant",
                   "notify_op_command", "notify_det_division", "firearm_reloaded", "sight_used"]
convert_to_time_stamp = ["trr_datetime", "trr_created", "status_datetime"]
convert_to_date = ["officer_appointed_date"]

yes_values = ["Y", "YES", "Yes", "yes"]
no_values = ["N", "NO", "No", "no"]

'''Variables for Checkpoint 2.2 (Data Reconciliation)'''
# officer_last_name - you may need to separate the last name from its suffix.
# officer_appointed_date - if the date is in the future, i.e., after 2021, subtract 100 years.
# subject_birth_year -  this one might require sanity checks, e.g., if you see a birth year of 40 then map it to 1940
# for years > 5 and less than 100
reconciliation_to_string = ["officer_first_name", "officer_last_name", "officer_race",
                            "officer_gender", "subject_race", "subject_gender",
                            "indoor_or_outdoor", "location", "street", "weapon_type", "party_fired_first"]
reconciliation_to_int = ["officer_birth_year", "subject_birth_year"]
reconciliation_to_date = ["officer_appointed_date"]

suffix_values = ["I", "II", "III", "IV", "V", "JR", "SR"]
male_gender_values = ["MALE", "Male"]
reconciled_male_value = "M"
female_gender_values = ["FEMALE", "Female"]
reconciled_female_value = "F"
race_values = ["BLACK", "AMER IND/ALASKAN NATIVE", "ASIAN/PACIFIC ISLANDER", "UNKNOWN", "WHITE", "HISPANIC"]
reconciled_race_values = ["Hispanic", "Black", "White", "Asian / Pacific", "Native American / Alaskan Native",
                          "Unknown"]
