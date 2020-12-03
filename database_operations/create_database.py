import sqlite3
from datetime import datetime

# Creating/Connecting the db
db_connection = sqlite3.connect('../Data/Database/job_database.db')

# Opening a cursor
db_cursor = db_connection.cursor()

# Create Table jobs to store scrapped jobs
db_cursor.execute("""CREATE TABLE job_details(
                    job_title text,
                    company_name text,
                    job_location text,
                    job_salary text,
                    job_description text,
                    job_posted text,
                    posted_website text,
                    job_link text NOT NULL PRIMARY KEY,
                    transaction_id int,
                    created_date_time text,
                    modified_date_time text
    )""")

# Create Table jobs to store transaction details
db_cursor.execute("""CREATE TABLE transaction_details(
                    transaction_id int NOT NULL PRIMARY KEY,
                    user_id text,
                    created_date_time text,
                    modified_date_time text
    )""")

# Create a zeroth record for transaction, so future one starts with 1
current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
insert_record = (0, 'admin', current_time, current_time)
db_cursor.execute('insert into transaction_details values (?,?,?,?)', insert_record)

# Commit the changes
db_connection.commit()

# Close the connection
db_connection.close()
