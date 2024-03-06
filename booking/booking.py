from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

import booking.cons as cons
from selenium.webdriver.common.by import By
import time

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self, currency=None):
        if currency != None:
            self.get(cons.BASE+"selected_currency="+currency)
        else:
            self.get(cons.BASE)

        self.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

    def skip(self):
        try:
            self.find_element(By.CSS_SELECTOR, '#b2indexPage > div.b9720ed41e.cdf0a9297c > div > div > div > div.dd5dccd82f > div.ffd93a9ecb.dc19f70f85.eb67815534 > div > button').click()
        except:
            print("Pop up not appeared")

    def select_destination(self, destination):
        self.find_element(By.ID, ':re:').send_keys(destination)
        time.sleep(1)
        self.find_element(By.ID, 'autocomplete-result-0').click()