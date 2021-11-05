import re

conn_string = "host='codd01.research.northwestern.edu' dbname='postgres' user='cpdbstudent' password='DataSci4AI'"

string_restructuring = re.compile(r"([.()!/-])")

fileNames = ["trr_trr_refresh", "trr_actionresponse_refresh", "trr_charge_refresh",
             "trr_weapondischarge_refresh", "trr_trrstatus_refresh", "trr_subjectweapon_refresh"]

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

location_values = ["AIRPORT PARKING LOT", "AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA",
                   "CHA HALLWAY / STAIRWELL / ELEVATOR", "CHA PARKING LOT / GROUNDS",
                   "CHURCH / SYNAGOGUE / PLACE OF WORSHIP", "COLLEGE / UNIVERSITY - GROUNDS",
                   "CTA PARKING LOT / GARAGE / OTHER PROPERTY", "FACTORY / MANUFACTURING BUILDING",
                   "GOVERNMENT BUILDING / PROPERTY", "HIGHWAY / EXPRESSWAY", "HOSPITAL BUILDING / GROUNDS",
                   "HOTEL / MOTEL", "LAKEFRONT / WATERFRONT / RIVERBANK", "MEDICAL / DENTAL OFFICE",
                   "MOVIE HOUSE / THEATER", "NURSING / RETIREMENT HOME", "OTHER RAILROAD PROPERTY / TRAIN DEPOT",
                   "OTHER (SPECIFY)", "PARKING LOT / GARAGE (NON RESIDENTIAL)", "POLICE FACILITY / VEHICLE PARKING LOT",
                   "RESIDENCE - GARAGE", "RESIDENCE - PORCH / HALLWAY", "RESIDENCE - YARD (FRONT / BACK)",
                   "SCHOOL - PRIVATE BUILDING", "SCHOOL - PRIVATE GROUNDS", "SCHOOL - PUBLIC BUILDING",
                   "SCHOOL - PUBLIC GROUNDS", "SPORTS ARENA / STADIUM", "TAVERN / LIQUOR STORE", "VACANT LOT / LAND",
                   "VEHICLE - COMMERCIAL", "VEHICLE - OTHER RIDE SHARE SERVICE (LYFT, UBER, ETC.)"]

reconciled_location_values = ["TAXICAB", "OTHER", "CHA APARTMENT", "HIGHWAY/EXPRESSWAY", "PARKING LOT/GARAGE("
                                                                                         "NON.RESID.)",
                              "AIRPORT EXTERIOR - NON-SECURE AREA", "CAR WASH", "ABANDONED BUILDING",
                              "LAKEFRONT/WATERFRONT/RIVERBANK", "DRUG STORE", "TAVERN/LIQUOR STORE",
                              "CHURCH/SYNAGOGUE/PLACE OF WORSHIP", "RESIDENTIAL YARD (FRONT/BACK)",
                              "NURSING HOME/RETIREMENT HOME", "FOREST PRESERVE", "FACTORY/MANUFACTURING BUILDING",
                              "GROCERY FOOD STORE", "AIRPORT/AIRCRAFT", "OTHER RAILROAD PROP / TRAIN DEPOT",
                              "WAREHOUSE", "CTA TRAIN", "DEPARTMENT STORE", "SCHOOL, PUBLIC, GROUNDS",
                              "CTA BUS STOP", "MEDICAL/DENTAL OFFICE", "RESIDENCE-GARAGE", "AIRPORT BUILDING "
                                                                                           "NON-TERMINAL - NON-SECURE "
                                                                                           "AREA", "AIRPORT TERMINAL "
                                                                                                   "UPPER LEVEL - "
                                                                                                   "NON-SECURE AREA",
                              "AIRPORT TERMINAL LOWER LEVEL - SECURE AREA", "CLEANING STORE", "ANIMAL HOSPITAL",
                              "SCHOOL, PRIVATE, GROUNDS", "HOSPITAL BUILDING/GROUNDS", "DAY CARE CENTER",
                              "CONSTRUCTION SITE", "GOVERNMENT BUILDING/PROPERTY", "SCHOOL, PRIVATE, BUILDING",
                              "RESIDENCE", "COIN OPERATED MACHINE", "COLLEGE/UNIVERSITY RESIDENCE HALL",
                              "BARBERSHOP", "GAS STATION", "HOTEL/MOTEL", "DRIVEWAY - RESIDENTIAL", "RESIDENCE "
                                                                                                    "PORCH/HALLWAY",
                              "CHA PARKING LOT/GROUNDS", "AIRPORT TRANSPORTATION SYSTEM (ATS)", "COLLEGE/UNIVERSITY "
                                                                                                "GROUNDS",
                              "SIDEWALK", "AIRPORT BUILDING NON-TERMINAL - SECURE AREA", "CURRENCY EXCHANGE",
                              "CTA BUS", "VACANT LOT/LAND", "CEMETARY", "BAR OR TAVERN", "POOL ROOM",
                              "BOWLING ALLEY", "OTHER COMMERCIAL TRANSPORTATION", "PARK PROPERTY", "AIRCRAFT",
                              "JAIL / LOCK-UP FACILITY", "VACANT PROPERTY", "VEHICLE - OTHER RIDE SERVICE",
                              "COMMERCIAL / BUSINESS OFFICE", "POLICE FACILITY/VEH PARKING LOT", "ALLEY", "LIBRARY",
                              "APPLIANCE STORE", "APARTMENT", "FIRE STATION", "MOVIE HOUSE/THEATER",
                              "CHA HALLWAY/STAIRWELL/ELEVATOR", "CTA GARAGE / OTHER PROPERTY", "STREET", "CONVENIENCE "
                                                                                                         "STORE",
                              "AIRPORT EXTERIOR - SECURE AREA", "VEHICLE-COMMERCIAL", "CTA PLATFORM", "SMALL RETAIL "
                                                                                                      "STORE",
                              "BANK", "CTA TRACKS - RIGHT OF WAY", "ATHLETIC CLUB", "SCHOOL, PUBLIC, BUILDING",
                              "SPORTS ARENA/STADIUM", "CTA STATION", "AIRPORT TERMINAL LOWER LEVEL - NON-SECURE "
                                                                     "AREA", "RESTAURANT", "AIRPORT TERMINAL UPPER "
                                                                                           "LEVEL - SECURE AREA",
                              "BRIDGE", "VEHICLE NON-COMMERCIAL"]

street_values = ["MIDWAY ST", "95TH PL", "C28 ST", "MIDWAY ST", "B2 ST", "ROOSEVELT", "NAPER AVE", "LUIS MUNOZ MARIN "
                                                                                                   "DR E",
                 "126TH PL", "CLEVELAND ST", "TAHOMA AVE", "LEYDEN AVE", "LEROY AVE", "L5 ST", "BEACH ST", "BEACH",
                 "BEECH ST", "INDIAN JOE ROAD", "GREGORY", "PONTIAC AVE", "I190 EXPY", "PARKING LOT E ST",
                 "HANSON AVE", "COLUMBIA DR", "L2 ST", "STRATFORD PL", "49TH AV", "ALBANY", "CONCOURSE A ST",
                 "GORDON AVE", "INTERNATIONAL PKWY", "EDENS EXPY IB", "CARVER PLZ", "STONE ST", "FARRAR DR", "GREEN",
                 "CRAIN ST", "DELPHIA AVE", "128TH PL", "EUGENIE ST", "47TH DR", "PARK RIDGE RD", "SHERWOOD AVE",
                 "BLOOMINGDALE TRL", "HARPER CT", "PAGE CT", "FOSTER PL", "GUNDERSON ST", "BROADWAY ST", "DAVOL ST",
                 "HOLDEN CT", "AVENUE E", "CONVENTION CENTER DRIVE", "HOWE ST", "KINGSDALE AVE", "173RD ST",
                 "MC DOWELL AVE", "K8 ST", "MILWAUKEE AV", "RAVEN ST", "ORLAND SQUARE DRIVE", "GORDON TER",
                 "MAGNET AVE", "17TH AVE.", "LOWER WACKER PL", "BELMONT HARBOR DR", "MARBLE PL", "ORLAND SQUARE DR",
                 "LUIS MUNOZ MARIN DR N"]

reconciled_street_values = ["FORD CITY DR", "PLYMOUTH CT", "COTTAGE GROVE", "DR MARTIN LUTHER KING JR DR", "CARVER DR", "126TH ST", "VAN VLISSINGEN RD", "66TH PL", "102ND PL", "125TH ST", "FOREST GLEN AVE", "43RD PL", "LYMAN ST", "24TH PL", "108TH ST", "22ND PL", "IRENE AVE", "LEAMINGTON AVE", "LATROBE AVE", "ADAMS ST", "BRENNAN AVE", "ROOSEVELT DR", "CENTRAL AVE", "MC CLURG CT", "LYNDALE ST", "55TH PL", "NEWCASTLE AVE", "SCHREIBER AVE", "122ND PL", "CORTLAND ST", "SACRAMENTO SD", "EXCHANGE AVE", "FULTON BLVD", "HUBBARD", "25TH ST", "DANIEL DR", "106TH ST", "RACINE AVE", "VINE ST", "BOULEVARD WAY", "PARK DR", "FRANCISCO AVE", "34TH PL", "71ST PL", "GENEVA TER", "BOSWORTH AVE", "WABASH", "PAULINA AVE", "CHICAGO BEACH DR", "MINERVA AVE", "SURF ST", "SPRINGFIELD AVE", "LE MOYNE ST", "RIDGE", "SIMONDS DR", "PRINCETON AVE", "BURNSIDE AVE", "BELLEVUE PL", "55TH AVE", "OAK PARK AVE", "115TH ST", "VIRGINIA AVE", "ASHLAND", "BISSELL ST", "77TH PL", "WENTWORTH AV", "MONROE DR", "86TH PL", "WALTON ST", "MARSHFIELD AVE", "COYLE AVE", "LONGWOOD DR", "121ST PL", "DELAWARE PL", "MEDILL AVE", "MASSASOIT AVE", "RIDGELAND AVE", "CALHOUN AVE", "MARSHALL", "PERRY AVE", "KOLMAR AVE", "61ST ST", "WENTWORTH AVE", "LAKE SHORE DR SB", "RIDGE AVE", "MILLARD AVE", "107TH ST", "CAMBRIDGE AVE", "HOYNE AVE", "CATALPA AVE", "JERSEY AVE", "CARROLL", "REDFIELD DR", "TRUMBULL AVE", "CITY FRONT PLAZA DR", "BAKER AVE", "RECREATION DR", "WISCONSIN ST", "OKETO", "SOUTH OAK PARK", "GIDDINGS ST", "MORSE AVE", "WINNECONNA PKWY", "37TH ST", "BISHOP FORD EXPY OB", "STETSON AVE", "DREW ST", "WARWICK AVE", "MARGATE TER", "LAWRENCE AVE", "STRONG ST", "NORMAL AVE", "19TH PL", "HENDERSON ST", "38TH PL", "112TH ST", "LAKE ST", "DAN RYAN LOCAL IB", "HADDON AVE", "58TH PL", "NORTH BLVD", "58TH ST", "ST GEORGES CT", "MORGAN DR", "KIRKLAND AVE", "WENDELL ST", "63RD ST", "KINZIE ST", "51ST ST", "RICE ST", "LAKE", "CARPENTER ST", "PAULINA ST", "JUNEWAY TER", "27TH ST", "CTA 69TH ST LN", "35TH PL", "STATE ST", "CLARK ST", "SANGAMON ST", "TOUHY AVE", "CTA 95TH ST LN", "HARRISON ST", "KING DR", "ARTHINGTON ST", "EISENHOWER EXPY IB", "DOUGLAS BLVD", "ELLIS AVE", "FULLERTON AVE", "CORCORAN PL", "RWY 14R", "MANNHEIM RD", "52ND ST", "ROCKWELL AVE", "21ST ST", "VERNON PARK PL", "FARRAGUT AVE", "KEELEY ST", "SEDGWICK ST", "15TH AVE", "STOCKTON DR", "ROBINSON ST", "JARVIS AVE", "OZARK AVE", "MONTVALE AVE", "40TH PL", "HOOD AVE", "57TH PL", "117TH PL", "MENARD AVE", "B12 ST", "WEST END AVE", "BARRY AVE", "36TH ST", "BISHOP ST", "15TH AVENUE", "HERMOSA AVE", "29TH ST", "WILLARD CT", "160 22ND", "FRANKLIN ST XR IB", "THOME AVE", "BALBO DR", "MORGAN ST", "RUTHERFORD AVE", "RUBLE ST", "CASTLE ISLAND AVE", "96TH ST", "30TH ST", "MUSKEGON AVE", "GALE ST", "GILBOU AVENUE", "33RD ST", "PARK", "EDMAIRE ST", "ILLINOIS ST", "GARFIELD SQUARE DR", "MERRIMAC AVE", "SOUTH WATER ST", "90 WEST", "I57 EXPY OB", "ONTARIO ST", "ESTES AVE", "ASHLAND AV", "PINE AVE", "ELMDALE AVE", "93RD ST", "DEARBORN ST", "BLUE ISLAND AVE", "ASHLAND BLVD", "SUPERIOR ST", "CLAREMONT AVE", "CHECKPOINT 3 ST", "MARQUETTE AVE", "DAN RYAN LOCAL OB", "HAMLET AVE", "WASECA PL", "MOZART ST", "LISTER AVE", "OLCOTT AVE", "68TH ST", "ARGYLE ST", "43RD ST", "CHICAGO", "MICHIGAN AV", "ALBION AVE", "WASHBURNE AVE", "AVERS AVE", "WINDSOR AVE", "WASHTENAW AVE", "HAYES AVE", "POTOMAC AVE", "LOGAN BLVD", "PARK SHORE EAST CT", "SCHUBERT AVE", "ST HELEN ST", "129TH PL", "BEACH AVE", "WALNUT ST", "AVENUE F", "113TH ST", "83RD PL", "CERMAK RD", "CUYLER AVE", "NORTH WATER ST", "ESCANABA AVE", "GREGORY ST", "IRVING AVE", "MARENGO", "MOBILE AVE", "51ST PL", "LAKE SHORE DR NB", "63RD PKWY", "ABERDEEN ST", "CICERO AVE", "KERFOOT AVE", "SACRAMENTO BLVD", "AVENUE O", "CLIFTON AVE", "NEWGARD AVE", "JEFFERSON ST", "BONFIELD ST", "CLYDE AVE", "118TH ST", "ROSEMONT AVE", "131ST PL", "91ST ST", "CALUMET", "MARQUETTE DR", "JEROME ST", "LA SALLE", "HOMAN BLVD", "STEVENSON EXPY IB", "HIGGINS AVE", "NEW ENGLAND AVE", "RIDGEWAY AVE", "HOHMAN AV", "NORA AVE", "BUENA AVE", "MONTGOMERY AVE", "BOWMANVILLE AVE", "PAXTON AVE", "FINANCIAL PL", "44TH PL", "THOMAS ST", "ODELL AVE", "AVENUE L", "CRIPPLE CREEK", "BONAPARTE ST", "KASSON AVE", "84TH PL", "86TH ST", "RUSSELL DR", "LOWELL AVE", "DORCHESTER AVE", "BREAKWATER ACCESS", "HARLEM AVE", "VANDERPOEL AVE", "DICKINSON AVE", "DIVERSEY AVE", "BRIAR PL", "SEMINARY AVE", "BOND AVE", "SAWYER AVE", "WHIPPLE ST", "KILPATRICK AVE", "LUMBER ST", "OZANAM AVE", "CHESTNUT ST", "CALDWELL AVE", "HOWARD ST", "MONTANA ST", "KILDARE", "63RD PL", "HIGGINS RD", "CENTRAL PARK AVE", "CATHERINE AVE", "YATES BLVD", "HERMIONE ST", "EAST RIVER RD", "HAYES ST", "75TH ST", "MONTICELLO AVE", "ANN STREET", "FRANCIS PL", "LINCOLN PARK WEST", "81ST ST", "KIMBALL AVE", "81 ST", "RAVENSWOOD AVE", "84TH ST", "PRATT AVE", "YATES AVE", "MAGNOLIA AVE", "GLENWOOD AVE", "INDEPENDENCE BLVD", "ERIE COURT", "SANDBURG TER", "MARKHAM AVE", "119TH PL", "WELLINGTON AVE", "FORRESTVILLE AVE", "CLARENDON AVE", "RUSH ST", "OKETO AVE", "KEDZIE AVE", "13TH ST", "MC LEAN AVE", "SCHILLER ST", "KOMENSKY AVE", "LEAVITT ST", "HAYES DR", "EGGLESTON AVE", "110TH ST", "120TH ST", "111TH PL", "HAMLIN BLVD", "CHASE AVE", "RACE AVE", "WALLEN AVE", "72ND ST", "105TH ST", "FULTON MARKET", "BURLING ST", "VAN BUREN ST", "106TH PL", "OAKWOOD BLVD", "LAKE SHORE DR", "PARKER AVE", "LOCUST ST", "PARK AVE", "STAVE ST", "4TH AVE", "RIDGE BLVD", "EASTLAKE TER", "BROAD ST", "LAPORTE AVE", "LEGETT AVE", "JANSSEN AVE", "NORMAL PKWY", "NORDICA AVE", "HASKINS AVE", "118TH PL", "OAKLEY AVE", "92ND ST", "87TH STREET", "IOWA ST", "124TH ST", "50TH ST", "WARREN BLVD", "DOUBLE EAGLE DRIVE", "62ND ST", "TALMAN AVE", "OCONTO AVE", "80TH PL", "57TH ST", "BRIGHTON PL", "CORNELL AVE", "MINOR ST.", "CRESCENT", "84 TH. ST.", "105TH PL", "WINONA ST", "HARPER AVE", "DOBSON AVE", "COULTER ST", "HILL ST", "CHURCH ST", "HARTWELL AVE", "WACKER DR", "BENSLEY AV", "OLEANDER AVE", "CENTRAL PARK BLVD", "EWING AVE", "PROSPECT AVE", "WISNER AVE", "WALLER AVE", "EMERALD AVE", "AVENUE C", "MINOR ST", "RIDGELAND", "FRANKLIN ST", "HENRY", "69TH PL", "LARRABEE ST", "GILES AVE", "KENNEDY EXPY IB", "DOTY AVE W", "82ND ST", "PALATINE AVE", "GOODMAN ST", "ESSEX AV", "94TH ST", "MAPLE ST", "79TH PL", "COLUMBIA AVE", "NASHVILLE AVE", "45TH PL", "DRAKE AVE", "MIDWAY PARK", "67TH PL", "ASHLAND AVE", "BIRCHWOOD AVE", "MYRTLE AVE", "PLAINFIELD AVE", "LITUANICA AVE", "KENSINGTON AVE", "LUTHER ST", "WOLFRAM ST", "133RD PL", "ORIOLE AVE", "116TH ST", "LOWER COLUMBUS DR", "64TH PL", "HUTCHINSON AVE", "WILCOX ST", "JEFFERY DR", "DREXEL SQUARE DR", "BELLE PLAINE AVE", "BENNETT AVE", "CHAMPLAIN AVE", "WILTON AVE", "33RD PL", "HALSTED SD", "OAKLEY BLVD", "BROWNING AVE", "FIELDING AVE", "48TH ST", "COTTAGE GROVE AVE", "FAIRBANKS CT", "133RD ST", "114TH ST", "SUNNYSIDE AVE", "BISHOP FORD EXPY IB", "FERDINAND ST", "OGDEN AVE", "LAKE PARK AVE", "KENNICOTT AVE", "LYON AVE", "104TH ST", "DAUPHIN AVE", "PEORIA ST", "MANGO AVE", "ROOSEVELT RD", "AVENUE H", "MALTA ST", "HARTLAND CT", "ESMOND ST", "123RD ST", "MILTIMORE AVE", "WILSON DR", "LYNN WHITE DR", "WESTGATE TER", "FLETCHER ST", "ORANGE AVE", "15TH ST", "SACRAMENTO DR", "CORLISS AVE", "CALUMET AVE", "HOMAN AVE"]

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
                        'officer_age', 'officer_unit_name', 'officer_unit_detail', 'trr_created', 'latitude',
                        'longitude',
                        'point', 'officer_id']

trr_trrstatus_refresh_cols = ['officer_rank', 'officer_star', 'status', 'status_datetime', 'officer_age',
                              'officer_unit_at_incident', 'trr_report_id', 'officer_id']

'''Variables for Checkpoint 4 ( Column Reordering )'''

final_file_names = ["trr_trr", "trr_actionresponse", "trr_charge", "trr_weapondischarge", "trr_trrstatus",
                    "trr_subjectweapon"]

final_columns = [

    ["id", "crid", "event_id", 'beat', 'block', 'direction', 'street', 'location', 'trr_datetime', 'indoor_or_outdoor',
     'lighting_condition', 'weather_condition', 'notify_OEMC', 'notify_district_sergeant', 'notify_OP_command',
     'notify_DET_division', 'party_fired_first', 'officer_assigned_beat', 'officer_on_duty', 'officer_in_uniform',
     'officer_injured', 'officer_rank', 'subject_armed', 'subject_injured', 'subject_alleged_injury', 'subject_age',
     'subject_birth_year', 'subject_gender', 'subject_race', 'officer_id', 'officer_unit_id', 'officer_unit_detail_id',
     'point']

    , ['person', 'resistance_type', 'action', 'other_description', 'trr_id']

    , ["statute", "description", "subject_no", "trr_id"]

    , ["weapon_type", "weapon_type_description", "firearm_make", "firearm_model", "firearm_barrel_length",
       "firearm_caliber", "total_number_of_shots", "firearm_reloaded", "number_of_cartridge_reloaded",
       "handgun_worn_type", "handgun_drawn_type", "method_used_to_reload", "sight_used", "protective_cover_used",
       "discharge_distance", "object_struck_of_discharge", "discharge_position", "trr_id"]

    , ["rank", "star", "status", "status_datetime", "officer_id", "trr_id"]

    , ["weapon_type", "firearm_caliber", "weapon_description", "trr_id"]]

trr_column_mismatch = ["cr_number", "event_number", "notify_oemc", "notify_op_command", "notify_det_division"]
trr_column_proper = ["crid", "event_id", "notify_OEMC", "notify_OP_command", "notify_DET_division"]
trr_status_column_mismatch = ["officer_rank", "officer_star"]
trr_status_column_proper = ["rank", "star"]
