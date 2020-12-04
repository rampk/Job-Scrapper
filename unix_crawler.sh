# Redirect logs for troubleshooting
exec 1> Data/logs/job_scrapper_unix.out 2> Data/logs/job_scrapper_unix.log


# Use the virtual environment
echo "Activating virtual environment"
venv/scripts/activate
echo "Activated virtual environment"

# Start the transacation
echo "Loading the transacation table"
cd database_operations
python start_transaction.py "guest"
echo "Loaded the transacation table"

cd ../jobscrapper_scrapy

# Scrapping the indeed website for Data Science jobscrapper_scrapy
# Have to rewite to accept and pass parameters

#echo "Started crawling indeed"
#scrapy crawl indeed -O ../Data/temp/indeed.csv
#echo "Completed crawling indeed"
echo "Started crawling simplyhired"
scrapy crawl simplyhired -O ../Data/temp/simplyhired.csv
echo "Completed crawling simplyhired"
#scrapy crawl workopolis -O ../Data/temp/workopolis.csv
#scrapy crawl wowjobs -O ../Data/temp/wowjobs.csv


# Cleaning the data
echo "Started loading data into DB"
cd ../database_operations
python loading_database.py 
echo "Loaded into DB"

echo "Process completed"
exit 0

#$SHELL