import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestSabzlearnScraper(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def tearDown(self):
        self.driver.close()

    def test_scrape_sabzlearn(self):
        driver = self.driver
        driver.get("https://www.sabzlearn.ir/")
        driver.maximize_window()
        time.sleep(10)

        # links with xpath
        links = driver.find_elements("xpath", "//div[contains(@class,'course')]//h4//a")

        # prices with xpath
        prices = driver.find_elements(
            "xpath", "//div[contains(@class,'course')]//span[contains(@class,'course__price')]"
        )

        self.assertEqual(len(links), len(prices))

        results = []
        for l in range(len(links)):
            results.append((links[l].get_attribute("href"), prices[l].text))

        self.assertEqual(len(results), 55)


if __name__ == '__main__':
    unittest.main()
