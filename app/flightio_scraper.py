import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def flightio_scrape(what: str, s_from: str, to: str, now):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    tickets = []
    s_from = s_from.upper()
    to = to.upper()
    for i in range(7):
        url = f"https://flightio.com/{what}/search/2/{s_from}-{to}%40/{(now + datetime.timedelta(days=i)).__str__()}/1-0-0-1"
        try:
            driver.get(url)
            driver.maximize_window()
            time.sleep(10)
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
            price = driver.find_elements("xpath",
                                         "//div[contains(@id,'DepartListSection')]//div[contains(@class, 'transition-inout-300')]//button[contains(@class,'!text-primary')]")

            for ticket in range(available.__len__()):
                s_time = when[ticket + ticket].text
                tickets.append(
                    {
                        "ticket": ticket,
                        "s_time": s_time,
                        "price": price[ticket].text
                    }
                )

        except:
            continue
    driver.close()
    return tickets
