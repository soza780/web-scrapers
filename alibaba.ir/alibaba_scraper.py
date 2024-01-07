from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

"""
    base url : https://www.alibaba.ir/train/THR-TBZ?adult=1&child=0&infant=0&ticketType=Family&isExclusive=false&departing=1402-11-05
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
        "//section[@class ='min-w-0']//div[contains(@class, 'a-card')][.//button]",
    )
    when = driver.find_elements(
        "xpath",
        "//section[@class ='min-w-0']//div[contains(@class, 'a-card')][.//button]//span[contains(@class,'text-5')][text()[contains(. ,':')]]",
    )
    
    for ticket in range(available.__len__()):
        s_time = when[ticket + ticket].text
        tickets.append(
            {
                "ticket": ticket,
                "s_time": s_time,
            }
        )
    with open("tickets.json", "w") as f:
        json.dump(tickets, f, indent=4)
    return tickets


if __name__ == "__main__":
    WHAT = input("What do you want to take (train,bus,flight)? ")
    ADULT_NUMBER = int(input("Enter the number of adults: "))
    FROM = input("From (ex: THR)")
    TO = input("To (ex:TBZ)")
    WHEN = input("when (ex: 1402-11-05)")
    base_url = f"https://www.alibaba.ir/{WHAT}/{FROM}-{TO}?adult={ADULT_NUMBER}&child=0&infant=0&ticketType=Family&isExclusive=false&departing={WHEN}"
    # base_url = "https://www.alibaba.ir/train/THR-TBZ?adult=1&child=0&infant=0&ticketType=Family&isExclusive=false&departing=1402-11-05"
    try:
        alibaba_scrape(base_url)
    except:
        raise Exception("something went wrong")
