from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def flightio_scrape(what: str,s_from: str, to: str, year: int,
                    month: int, day: int,day_of_month: int) -> list:
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    for i in range(7):
        url = f"https://flightio.com/{what}/search/2/{s_from}-{to}%40/{year}-{month}-{day_of_month}/1-0-0-1"
        if day_of_month + i > 31:
            url = url = f"https://flightio.com/{what}/search/2/{s_from}-{to}%40/{year}-{month + 1}-{1}/1-0-0-1"
        try:
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
            
            return tickets
        except:
            continue