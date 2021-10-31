import pandas as pd
from read_data import *

if __name__ == '__main__':

    fileNames = ["trr_trr_refresh.csv", "trr_trr_actionresponse_refresh.csv", "trr_charge_refresh.csv",
                 "trr_subjectweapon_refresh.csv", "trr_trrstatus_refresh.csv", "trr_weapondischarge_refresh.csv"]

    # Load the first file from the csv to pandas dataframe
    trr_trr_refresh = loadFile("trr_trr_refresh.csv")
    trr_trr_refresh.info()

    # 1st Step:
    # replace the ‘officer_on_duty' column contains
    # the values 'Y' and 'N'  with
    # True and  False:
    trr_trr_refresh['officer_on_duty'] = trr_trr_refresh['officer_on_duty'].map({'Y': 1, 'N': 0})

    print(trr_trr_refresh["officer_on_duty"])
