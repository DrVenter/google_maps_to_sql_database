import numpy as np
import pandas as pd
from sqlalchemy import create_engine

"""
this script creates a MySQL table in a database.
Note: ensure sqlalchemy and PyMySQL are installed before use.
"""

def use_sqlalchemy_to_connect_to_database(database_name):
	host_name = "LocalHost"
	database_name = database_name
	user_name = "root"
	password = input("Enter password: ")

	sql_engine = create_engine(f"mysql+pymysql://{user_name}:{password}@{host_name}/{database_name}")

	return sql_engine

def convert_data_frame_to_mysql_database(dataframe, table_name):
	dataframe.to_sql(table_name, use_sqlalchemy_to_connect_to_database("tattoo_database"), index=False)

database = pd.read_csv("tattoo_studios_database.csv")
convert_data_frame_to_mysql_database(database, "tattoo_studios")
print("Database COnversion Successful!")