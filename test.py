import sqlite3

db_connection = sqlite3.connect('../Data/Database/job_database.db')

db_cursor = db_connection.cursor()
db_cursor.execute('select * from job_details')
print(db_cursor.fetchall())
