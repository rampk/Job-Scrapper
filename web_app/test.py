import sqlite3
from data_transformation import arrange_columns

db_connection = sqlite3.connect('../Data/Database/job_database.db')
db_cursor = db_connection.cursor()

db_cursor.execute("select job_link from job_details")
print(db_cursor.fetchall())

job_data = arrange_columns()

job_data.to_csv('simplyhired.csv')