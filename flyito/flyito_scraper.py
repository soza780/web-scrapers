from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

"""
    base url : https://flightio.com/flight/search/2/THR-SYZ%40/2024-02-05/1-0-0-1
"""


def alibaba_scrape(url: str):
    """
    Scrapes the Alibaba website for tickets and prices.
    """
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)
    tickets = []
    tickets.append(
        {
            "site": url,
            "time": time.ctime(),
        }
    )
    # "//section[@class ='min-w-0']//div[contains(@class, 'a-card')]" => every single card in  site
    available = driver.find_elements(
        "xpath",
        "//div[contains(@id,'DepartListSection')]//div[contains(@class, 'transition-inout-300')]",
    )
    when = driver.find_elements(
        "xpath",
        "//div[contains(@id,'DepartListSection')]//span[text()[contains(.,':')]]",
    )
    price = driver.find_elements("xpath", "//div[contains(@id,'DepartListSection')]//div[contains(@class, 'transition-inout-300')]//button[contains(@class,'!text-primary')]")

    for ticket in range(available.__len__()):
        s_time = when[ticket + ticket].text
        tickets.append(
            {
                "ticket": ticket,
                "s_time": s_time,
                "price": price[ticket].text
            }
        )
    with open("flyitotickets.json", "w") as f:
        json.dump(tickets, f, indent=4)
    return tickets


if __name__ == "__main__":
    # WHAT = input("What do you want to take (train,bus,flight)? ")
    # ADULT_NUMBER = int(input("Enter the number of adults: "))
    # FROM = input("From (ex: THR)")
    # TO = input("To (ex:TBZ)")
    # WHEN = input("when (MILADI)")
    # base_url = f"https://flightio.com/{WHAT}/search/2/{FROM}-{TO}%40/{WHEN}/1-0-0-1"
    base_url = "https://flightio.com/flight/search/2/THR-SYZ%40/2024-02-05/1-0-0-1"
    alibaba_scrape(base_url)


"""
//div[contains(@id,'DepartListSection')]  kol blita 
"""