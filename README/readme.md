# SPA scraper with python and selenium

![Selenium image](selenium.png)

## Disclaimer

This project is for educational purposes only. Web scraping can be considered an unethical practice and is against the
terms of service of many websites. The use of this project for any unlawful or malicious purposes is not advised and the
author will not be held responsible for any damages or legal repercussions that may arise from its use.

## about

this repository is going to be a collection of SPA Scraper  implementations. as you may know , single page webapplications
are hard to scrape data from, because it takes time for javascript to do something and generate stuff.

so there would be an option to implement scraper with selenium webdriver and use sleep a little bit to page become ready
for scraping

## list of scrapers

- alibaba.ir
- flytoday.ir
- flightio
  
## use case
if you live in iran :) and you need to find a ticket,(filght, train, bus ..) and you cant find it
this script will help you.
make sure you close every chrome window or tab first then try to run the main.py in app folder
for linux:
```
python3 main.py
```
or in windows
```
python main.py
```
you can see chrome browser will pop up multiple time and will go thorgh couple of pages and do the stuff
after that a tickets.json file would appear in project directory.
if you open that you can see all the tickets that was availble in those websites.

i need to mention that there are issues in the script and in would get better in future.

regards <3


