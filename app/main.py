from app.alibaba_scraper import alibaba_scrape
import json

def main():
    ALL_TICKETS = []
    WHAT = input("what do you want ,flight, train ...")
    S_FORM = input("from...")
    TO = input("to...")
    YEAR = int(input("year"))
    MONTH = int(input("month"))
    DAY = int(input("day"))
    try:
        ALL_TICKETS.append(alibaba_scraper.alibaba_scrape(WHAT,S_FORM,TO,YEAR,MONTH,DAY))
        ALL_TICKETS.append(flightio_scraper.flghtio_scrape(WHAT,S_FORM,TO,YEAR,MONTH,DAY))
        ALL_TICKETS.append(flytoday_scraper.flytoday_scrape(WHAT,S_FORM,TO,YEAR,MONTH,DAY))
        with open("tickets.json", "w") as f:
                json.dump(ALL_TICKETS, f, indent=4)
    except:
        raise Exception("app.main error while trying to call scraper functions")
        


if __name__ == "__main__":
     main()      