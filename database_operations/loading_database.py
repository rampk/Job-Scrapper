import sys
import sqlite3
import pandas as pd
from os import listdir, remove
from data_transformation import arrange_columns
from data_transformation import unique_jobs
from datetime import datetime


def load_transaction(user, rows_fetched, unique_rows, current_transaction, current_time):
    # connecting to the db
    db_connection = sqlite3.connect('../Data/Database/job_database.db')
    db_cursor = db_connection.cursor()

    # insert current transaction details
    insert_record = (current_transaction, user, rows_fetched, unique_rows,
                     current_time, current_time)
    db_cursor.execute('insert into transaction_details values (?,?,?,?,?,?)', insert_record)
    db_connection.commit()
    db_connection.close()


def load_create_jobs(user):
    # arrange the columns and return all records as single file
    job_data = arrange_columns()
    rows_fetched = job_data.shape[0]

    # connect to the database
    db_connection = sqlite3.connect('../Data/Database/job_database.db')
    db_cursor = db_connection.cursor()

    # Check the DB and extract the unique jobs
    job_links = pd.read_sql('select job_link from job_details', db_connection)
    unique_job_data = unique_jobs(job_links, job_data)
    unique_rows = unique_job_data.shape[0]

    # saving the final output
    unique_job_data.to_csv('../Data/final/new_jobs.csv', index=False)

    # fetch the last transaction and time
    db_cursor.execute('select max(transaction_id) from transaction_details')
    last_transaction = db_cursor.fetchall()[0][0]
    current_transaction = last_transaction + 1
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # insert transaction details
    load_transaction(user, rows_fetched, unique_rows, current_transaction, current_time)

    # writing the transaction details to the dataframe
    unique_job_data['transaction_id'] = current_transaction
    unique_job_data['created_date_time'] = current_time
    unique_job_data['modified_date_time'] = current_time

    if not unique_job_data.empty:
        unique_job_data.to_sql('job_details', db_connection, if_exists='append', index=False)

    db_connection.close()


def clean_temp():
    file_list = listdir('../Data/temp')
    for file in file_list:
        file_path = '../Data/temp/' + file
        remove(file_path)


load_create_jobs(sys.argv[1])
clean_temp()
