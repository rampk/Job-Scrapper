# Use the virtual environment
source venv/scripts/activate

cd jobscrapper_scrapy

# Scrapping the indeed website for Data Science jobscrapper_scrapy
# Have to rewite to accept and pass parameters

scrapy crawl indeed -O ../Data/temp/indeed.csv
scrapy crawl simplyhired -O ../Data/temp/simplyhired.csv
scrapy crawl workopolis -O ../Data/temp/workopolis.csv
scrapy crawl wowjobs -O ../Data/temp/wowjobs.csv


# Cleaning the data
cd ../database_operations
python loading_database.py "admin"


$SHELL