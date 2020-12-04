import sqlite3

# Connect to the DB
db_connection = sqlite3.connect('../Data/Database/job_database.db')
db_cursor = db_connection.cursor()

# Get the current transaction number
db_cursor.execute('select max(transaction_id) from transaction_details')
current_transaction = (db_cursor.fetchall()[0][0],)

# Update transaction status as completed
db_cursor.execute("""update transaction_details  
                     set transaction_ended = 1
                     where transaction_id = ?""", current_transaction)

# Close the connection
db_connection.commit()
db_connection.close()
