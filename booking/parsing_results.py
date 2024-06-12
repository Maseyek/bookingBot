from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.by import By

class ParsingResults:
    def __init__(self, page_results: List[WebElement]):
        self.page_results = page_results
        print(len(self.page_results))

    def title(self):
        for result in self.page_results:
            print(result.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute('innerHTML').strip())
