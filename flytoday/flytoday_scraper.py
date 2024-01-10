from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

"""
https://www.flytoday.ir/flight/search?departure=thr,1&arrival=mhd,1&departureDate=2024-01-19&adt=1&chd=0&inf=0&cabin=1&isDomestic=true
"""
def flytoday_scrape(url: str):
    """
    Scrapes the flytoday website for tickets and prices.
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
    with open("flytodaytickets.json", "w") as f:
        json.dump(tickets, f, indent=4)
    return tickets


if __name__ == "__main__":
    WHAT = input("What do you want to take (train,bus,flight)? ")
    ADULT_NUMBER = int(input("Enter the number of adults: "))
    FROM = input("From (ex: THR)")
    FROM = FROM.lower()
    TO = input("To (ex:TBZ)")
    TO = TO.lower()
    WHEN = input("when (MILADI)")
    # base_url = f"https://flightio.com/{WHAT}/search/2/{FROM}-{TO}%40/{WHEN}/1-0-0-1"
    base_url = f"https://www.flytoday.ir/{WHAT}/search?departure={FROM},1&arrival={TO},1&departureDate={WHEN}&adt={ADULT_NUMBER}&chd=0&inf=0&cabin=1&isDomestic=true"
    flytoday_scrape(base_url)