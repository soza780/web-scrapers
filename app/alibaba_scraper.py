import time

import jdatetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def alibaba_scrape(what: str, s_from: str, to: str, now):
    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    s_from = s_from.upper()
    to = to.upper()
    s_date = jdatetime.date.fromgregorian(year=now.year, month=now.month, day=now.day)
    tickets = []
    for i in range(7):
        if what == "flight":
            url = f"https://www.alibaba.ir/{what}s/{s_from}-{to}?adult=1&child=0&infant=0&departing={s_date.year}-{s_date.month}-{s_date.day + i}"
        else:
            url = f"https://www.alibaba.ir/{what}/{s_from}-{to}?adult=1&child=0&infant=0&departing={s_date.year}-{s_date.month}-{s_date.day + i}"

        try:
            driver.get(url)
            driver.maximize_window()
            time.sleep(10)
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
    driver.close()
    return tickets
