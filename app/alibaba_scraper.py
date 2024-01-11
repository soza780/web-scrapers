from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

"""
    base url : https://www.alibaba.ir/train/THR-TBZ?adult=1&child=0&infant=0&ticketType=Family&isExclusive=false&departing=1402-11-05
"""


def alibaba_scrape(what: str,s_from: str, to: str, year: int,
                    month: int, day: int,day_of_month: int):
  
    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    s_from = s_from.upper()
    to = to.upper()
    for i in range(7):
        url = f"https://www.alibaba.ir/{what}/{s_from}-{to}?adult=1&child=0&infant=0&ticketType=Family&isExclusive=false&departing={year}-{month}-{day_of_month + i}"
        if day_of_month + i > 31:
            url = f"https://www.alibaba.ir/{what}/{s_from}-{to}?adult=1&child=0&infant=0&ticketType=Family&isExclusive=false&departing={year}-{month + 1}-{i}"
        try:
            driver.get(url)
            driver.maximize_window()
            time.sleep(10)
            tickets = []
            available = driver.find_elements(
                "xpath",
                "//section[@class ='min-w-0']//div[contains(@class, 'a-card')][.//button]",
            )
            when = driver.find_elements(
                "xpath",
                "//section[@class ='min-w-0']//div[contains(@class, 'a-card')][.//button]//span[contains(@class,'text-5')][text()[contains(. ,':')]]",
            )
            tickets.append(
                {
                    "site": url,
                    "time": time.ctime(),
                }
            )

            for ticket in range(available.__len__()):
                s_time = when[ticket + ticket].text
                tickets.append(
                    {
                        "ticket": ticket,
                        "s_time": s_time,
                    }
                )
            
        except:
            continue
        return tickets
