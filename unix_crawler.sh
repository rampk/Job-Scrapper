# Use the virtual environment
source venv/scripts/activate

which pip
which python
cd jobscrapper_scrapy

# Scrapping the indeed website for Data Science jobscrapper_scrapy
# Have to rewite to accept and pass parameters

scrapy crawl indeed -O ../Data/temp/indeed.csv



$SHELL

