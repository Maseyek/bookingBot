from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class Filters:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # values available 0-5
    def star_rating(self, *ratings):
        for element in ratings:
            self.driver.find_element(By.CSS_SELECTOR, f'input[name="class={element}"][value="class={element}"]').click()
