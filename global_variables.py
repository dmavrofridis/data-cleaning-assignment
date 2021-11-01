conn_string = "host='codd01.research.northwestern.edu' dbname='postgres' user='cpdbstudent' password='DataSci4AI'"

convert_to_int = ["beat", "officer_birth_year", "officer_age", "subject_birth_year", "subject_age", "officer_birth_year"]
convert_to_bool = ["officer_on_duty", "officer_injured", "officer_in_uniform", "subject_armed",
                   "subject_injured", "subject_alleged_injury", "notify_oemc", "notify_district_sergeant",
                   "notify_op_command", "notify_det_division", "firearm_reloaded", "sight_used"]
convert_to_time_stamp = ["trr_datetime", "trr_created", "status_datetime"]
convert_to_date = ["officer_appointed_date"]