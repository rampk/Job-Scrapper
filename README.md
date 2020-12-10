# Job-Scrapper
**Languages Used:** Python, Unix Shell Script, SQL, HTML<br>
**Frameworks Used:** Scrapy, Flask<br>
**Database Used:** Sqlite3<br><br>
Currently Job Scrapper supports scrapping Indeed, Workopolis, Simplyhired, and Wowjobs. This application can be used to scrap information about the Canadian jobs and store it in DB and as CSV.<br> 
### Technical flow diagram
<img src="https://github.com/rampk/Job-Scrapper/blob/master/Data/Job%20Scraper%20flow.png" width="846" height="500"><br><br>
#### How to run the application?<br>
Run start_flash.sh script to open the web app interacts with the application and the user. The web app will run in port 5000 (if it is available during the current session), and it can be accessed from http://127.0.0.1:5000/home.<br><br>
<img src="https://github.com/rampk/Job-Scrapper/blob/master/Data/Webapp%20Interface.png" width="500" height="300"><br><br>
#### Where to check for Scraped data?<br>
All scrapped data are stores in database (can be found in Data/Database folder), and output for each transcation is stored in a CSV file (can be found in Data/final folder)
