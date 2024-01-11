from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime



def flytoday_scrape(what: str,s_from: str, to: str,now):
    """
    Scrapes the flytoday website for tickets and prices.
    """
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    tickets = []
    s_from = s_from.lower()
    to = to.lower()
    for i in range(7):
        url = f"https://www.flytoday.ir/{what}/search?departure={s_from},1&arrival={to},1&departureDate={(now + datetime.timedelta(days=i)).__str__()}&adt=1&chd=0&inf=0&cabin=1&isDomestic=true"
    
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
            # "//div[@class = 'itineraries-container_itineraryWrapper__0NEnY'] " => every single card in  site
            available = driver.find_elements(
                "xpath",
                "//div[@class = 'itineraries-container_itineraryWrapper__0NEnY']",
            )
            # more_button = driver.find_element("xpath", "//button[.//span[text()='نمایش بیشتر']]").click()

            when = driver.find_elements(
                "xpath",
                "//div[@class = 'itineraries-container_itineraryWrapper__0NEnY']//div[contains(@class,'route-two-line-part_routeTwoLineTopPart__JWDky')]//div[contains(@class,'tooltip_tooltipWrapper__1mabM')]",
            )
            price = driver.find_elements("xpath", "//div[@class = 'itineraries-container_itineraryWrapper__0NEnY']//div[contains(@class,'d-flex')][contains(@class,'text-secondary-green ')]")

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

