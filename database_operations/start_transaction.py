import sys
import sqlite3
from datetime import datetime


def start_transaction(user):
    # connecting to the db
    db_connection = sqlite3.connect('../Data/Database/job_database.db')
    db_cursor = db_connection.cursor()

    # fetch the last transaction and time
    db_cursor.execute('select max(transaction_id) from transaction_details')
    last_transaction = db_cursor.fetchall()[0][0]
    current_transaction = last_transaction + 1
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    insert_record = (current_transaction, user, 1, 0, 0, 0,
                     current_time, current_time)
    db_cursor.execute('insert into transaction_details values (?,?,?,?,?,?,?,?)', insert_record)

    # Close the connection
    db_connection.commit()
    db_connection.close()


start_transaction(sys.argv[1])
