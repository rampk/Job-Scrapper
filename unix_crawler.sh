# Redirect logs for troubleshooting
exec 1> Data/logs/job_scrapper_unix.out 2> Data/logs/job_scrapper_unix.log
set -x

### Writing the script start time
time=`date`
echo "Script start_time" $time


# Reading the inputs passed
job_title=$1
job_location=$2
job_websites=$3
echo "Received" $job_title $job_location $job_websites

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

printf '=%.0s' {1..100}
echo ""
scrap_start=`date`
echo "Scrapping start time" $time

if [[ $job_websites == *"simplyhired"* ]]; then
	
	time==`date`
	echo "Started crawling simplyhired"
	scrapy crawl simplyhired -O ../Data/temp/simplyhired.csv -a job_title=$job_title
	scraped_time=`date`
	runtime=$(($scraped_time - $time))
	echo "Completed simplyhired in"$runtime
fi

if [[ $job_websites == *"indeed"* ]]; then
	
	time==`date`
	echo "Started crawling indeed"
	scrapy crawl indeed -O ../Data/temp/indeed.csv -a job_title=$job_title -a job_location=$job_location
	scraped_time=`date`
	runtime=$(($scraped_time - $time))
	echo "Completed indeed in"$runtime

fi

if [[ $job_websites == *"wowjobs"* ]]; then

	time==`date`
	echo "Started crawling wowjobs"
	scrapy crawl wowjobs -O ../Data/temp/wowjobs.csv -a job_title=$job_title
	scraped_time=`date`
	runtime=$(($scraped_time - $time))
	echo "Completed wowjobs in"$runtime

fi

if [[ $job_websites == *"workopolis"* ]]; then

	time==`date`
	echo "Started crawling workopolis"
	scrapy crawl workopolis -O ../Data/temp/workopolis.csv -a job_title=$job_title 
	scraped_time=`date`
	runtime=$(($scraped_time - $time))
	echo "Completed workopolis in"$runtime

fi

scrap_end=`date`
runtime=$(($scrap_end - $scrap_start))
echo "Completed overall scrapping in" $runtime
printf '=%.0s' {1..100}
echo ""

# Cleaning the data
echo "Started loading data into DB"
cd ../database_operations
python loading_database.py 
echo "Loaded into DB"

echo "Process completed"
exit 0

#$SHELL