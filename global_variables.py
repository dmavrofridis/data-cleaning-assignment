import re

conn_string = "host='codd01.research.northwestern.edu' dbname='postgres' user='cpdbstudent' password='DataSci4AI'"

string_restructuring = re.compile(r"([.()!/-])")

fileNames = ["trr_trr_refresh", "trr_actionresponse_refresh", "trr_charge_refresh",
             "trr_subjectweapon_refresh", "trr_trrstatus_refresh", "trr_weapondischarge_refresh"]

'''Variables for Checkpoint 2.1 (Data Cleaning)'''
convert_to_int = ["beat", "officer_birth_year", "officer_age", "subject_birth_year", "subject_age"]
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

location_values = ["AIRPORT PARKING LOT", "AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA", "CHA HALLWAY / STAIRWELL / ELEVATOR", "CHA PARKING LOT / GROUNDS", "CHURCH / SYNAGOGUE / PLACE OF WORSHIP", "COLLEGE / UNIVERSITY - GROUNDS", "CTA PARKING LOT / GARAGE / OTHER PROPERTY", "FACTORY / MANUFACTURING BUILDING", "GOVERNMENT BUILDING / PROPERTY", "HIGHWAY / EXPRESSWAY", "HOSPITAL BUILDING / GROUNDS", "HOTEL / MOTEL", "LAKEFRONT / WATERFRONT / RIVERBANK", "MEDICAL / DENTAL OFFICE", "MOVIE HOUSE / THEATER", "NURSING / RETIREMENT HOME", "OTHER RAILROAD PROPERTY / TRAIN DEPOT", "OTHER (SPECIFY)", "PARKING LOT / GARAGE (NON RESIDENTIAL)", "POLICE FACILITY / VEHICLE PARKING LOT", "RESIDENCE - GARAGE", "RESIDENCE - PORCH / HALLWAY", "RESIDENCE - YARD (FRONT / BACK)", "SCHOOL - PRIVATE BUILDING", "SCHOOL - PRIVATE GROUNDS", "SCHOOL - PUBLIC BUILDING", "SCHOOL - PUBLIC GROUNDS", "SPORTS ARENA / STADIUM", "TAVERN / LIQUOR STORE", "VACANT LOT / LAND", "VEHICLE - COMMERCIAL", "VEHICLE - OTHER RIDE SHARE SERVICE (LYFT, UBER, ETC.)"]

reconciled_location_values = ["Appliance Store", "Factory/Manufacturing Building", "Apartment", "Government Building/Property", "Parking Lot/Garage(Non.Resid.)", "Airport Building Non-Terminal - Secure Area", "College/University Residence Hall", "Alley", "Cemetary", "Commercial / Business Office", "Vacant Property", "Bowling Alley", "Hospital Building/Grounds", "Cta Platform", "Gas Station", "Movie House/Theater", "Cta Bus", "Other", "Cta Garage / Other Property", "Vehicle Non-Commercial", "Cha Apartment", "School, Private, Grounds", "Sports Arena/Stadium", "Cleaning Store", "Athletic Club", "School, Public, Grounds", "Vehicle-Commercial", "School, Public, Building", "Medical/Dental Office", "Airport/Aircraft", "Airport Terminal Upper Level - Non-Secure Area", "Hotel/Motel", "Nursing Home/Retirement Home", "Highway/Expressway", "Construction Site", "Barbershop", "Tavern/Liquor Store", "Lakefront/Waterfront/Riverbank", "Jail / Lock-Up Facility", "Car Wash", "Airport Terminal Lower Level - Non-Secure Area", "Department Store", "Drug Store", "Airport Exterior - Non-Secure Area", "Convenience Store", "Other Commercial Transportation", "Residence Porch/Hallway", "School, Private, Building", "Bridge", "Police Facility/Veh Parking Lot", "Animal Hospital", "Currency Exchange", "Airport Terminal Lower Level - Secure Area", "Cta Tracks - Right Of Way", "Taxicab", "Sidewalk", "Street", "Residence-Garage", "Abandoned Building", "Bank", "Forest Preserve", "Airport Building Non-Terminal - Non-Secure Area", "Grocery Food Store", "Driveway - Residential", "Airport Exterior - Secure Area", "Church/Synagogue/Place Of Worship", "Airport Terminal Upper Level - Secure Area", "Restaurant", "Library", "Residential Yard (Front/Back)", "Vacant Lot/Land", "Airport Transportation System (Ats)", "Warehouse", "Fire Station", "Park Property", "Cha Parking Lot/Grounds", "Vehicle - Other Ride Service", "Cha Hallway/Stairwell/Elevator", "Cta Bus Stop", "Small Retail Store", "Other Railroad Prop / Train Depot", "College/University Grounds", "Cta Station", "Aircraft", "Day Care Center", "Bar Or Tavern", "Residence", "Pool Room", "Coin Operated Machine", "Cta Train"]


'''Variables for Checkpoint 3 Data Integration (Linking the Officers)'''
# first name, middle initial, last name, suffix name, birth year, appointed date, gender, race
match_columns_org = ["first_name", "middle_initial", "last_name", "birth_year", "appointed_date",
                     "gender", "race", "suffix_name"]

match_columns_refresh = ["officer_first_name", "officer_middle_initial", "officer_last_name",
                         "officer_birth_year", "officer_appointed_date", "officer_gender", "officer_race",
                         "officer_suffix"]

new_columns = ["officer_id", "officer_unit_id", "officer_unit_detail_id"]

# This is a list which contains the name of the columns that we have to drop when mergin tables
# first_name, middle_initial, last_name, suffix_name (if applicable), gender, race, appointed_date, birth year
columns_to_drop = ["officer_first_name", "officer_middle_initial", "officer_last_name",
                   "officer_birth_year", "officer_appointed_date", "officer_gender", "officer_race",
                   "officer_suffix"]

trr_trr_refresh_cols = ['id', 'event_number', 'cr_number', 'beat', 'block', 'direction',
                        'street', 'location', 'trr_datetime', 'indoor_or_outdoor', 'lighting_condition',
                        'weather_condition', 'notify_oemc', 'notify_district_sergeant', 'notify_op_command',
                        'notify_det_division', 'party_fired_first', 'officer_assigned_beat', 'officer_on_duty',
                        'officer_in_uniform', 'officer_injured', 'officer_rank', 'subject_armed', 'subject_injured',
                        'subject_alleged_injury', 'subject_age', 'subject_birth_year', 'subject_gender', 'subject_race',
                        'officer_age', 'officer_unit_name', 'officer_unit_detail', 'trr_created', 'latitude', 'longitude',
                        'point', 'officer_id']

trr_trrstatus_refresh_cols = ['officer_rank', 'officer_star', 'status', 'status_datetime', 'officer_age',
                              'officer_unit_at_incident', 'trr_report_id', 'officer_id']

