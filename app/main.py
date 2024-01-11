from alibaba_scraper import alibaba_scrape
from flightio_scraper import flightio_scrape
from flytoday_scraper import flytoday_scrape
import jdatetime, datetime
import json
now = datetime
def main():
    ALL_TICKETS = []
    WHAT = input("what do you want ,flight, train ...")
    S_FORM = input("from...")
    TO = input("to...")
    NOW = datetime.date.today()

    ALL_TICKETS.append(alibaba_scrape(WHAT,S_FORM,TO,NOW))
    ALL_TICKETS.append(flightio_scrape(WHAT,S_FORM,TO,NOW))
    ALL_TICKETS.append(flytoday_scrape(WHAT,S_FORM,TO,NOW))
    with open("tickets.json", "w") as f:
        json.dump(ALL_TICKETS, f, indent=4)



if __name__ == "__main__":
     main()      