import psycopg2
from global_variables import *


def connect_to_db():
    return psycopg2.connect(conn_string)
