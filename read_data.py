import pandas as pd
import psycopg2
from global_variables import *


def loadFile(fileName):
    return pd.read_csv(fileName)


def connect_to_db():
    return psycopg2.connect(conn_string)


