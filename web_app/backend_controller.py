from input_operations import process_inputs
import subprocess
import sqlite3


def run_script(job_title, job_location, job_websites):
    # Clean the inputs
    job_title, job_location, job_websites = process_inputs(job_title, job_location, job_websites)
    # Run the script
    subprocess.Popen(['unix_crawler.sh', job_title, job_location, job_websites], cwd="../", shell=True)


def is_running():
    db_connection = sqlite3.connect('../Data/Database/job_database.db')
    db_cursor = db_connection.cursor()

    # Get the current transaction number
    db_cursor.execute('select max(transaction_id) from transaction_details')
    current_transaction = (db_cursor.fetchall()[0][0],)

    # Check whether transaction is running
    db_cursor.execute("""select transaction_ended from transaction_details
                            where transaction_id = ? """, current_transaction)
    transaction_status = db_cursor.fetchall()[0][0]
    return transaction_status == 0
