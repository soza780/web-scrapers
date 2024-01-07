"""
This script uses Selenium to scrape the Sabzlearn website for course links and prices.

Usage:
1. Install the required packages using pip:
pip install selenium
pip install webdriver-manager
2. Run the script and provide the URL of the Sabzlearn website as an argument.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_sabzlearn(url: str):
    """
    Scrapes the Sabzlearn website for course links and prices.

    Args:
        url (str): The URL of the Sabzlearn website.

    Returns:
        A list containing the course links and prices.
    """
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)

    # links with xpath
    links = driver.find_elements("xpath", "//div[contains(@class,'course')]//h4//a")

    # prices with xpath
    prices = driver.find_elements(
        "xpath", "//div[contains(@class,'course')]//span[contains(@class,'course__price')]"
    )

    results = []
    for l in range(len(links)):
        results.append((links[l].get_attribute("href"), prices[l].text))

    driver.close()
    return results


if __name__ == "__main__":
    url = input("Enter the URL of the Sabzlearn website: ")
    results = scrape_sabzlearn(url)
    for link, price in results:
        print(f"Link: {link}\nPrice: {price}")
