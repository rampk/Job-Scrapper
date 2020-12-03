import sqlite3

# Creating/Connecting the db
db_connection = sqlite3.connect('Data/Database/job_database.db')

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
                    job_link text,
                    transaction_id int,
                    created_date_time text,
                    modified_date_time text
    )""")

# Create Table jobs to store transaction details
db_cursor.execute("""CREATE TABLE transaction_details(
                    transaction_id int,
                    user_id text,
                    created_date_time text,
                    modified_date_time text
    )""")

# Commit the changes
db_connection.commit()

# Close the connection
db_connection.close()
