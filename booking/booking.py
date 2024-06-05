from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

import booking.cons as cons
from selenium.webdriver.common.by import By
import time
from booking.filters import Filters

options = Options()
options.add_experimental_option("detach", True)


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
        if currency is not None:
            self.get(cons.BASE + "selected_currency=" + currency)
        else:
            self.get(cons.BASE)

        self.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

    def skip(self):
        try:
            self.find_element(By.CSS_SELECTOR,
                              '#b2indexPage > div.b9720ed41e.cdf0a9297c > div > div > div > div.dd5dccd82f > div.ffd93a9ecb.dc19f70f85.eb67815534 > div > button').click()
        except:
            print("Pop up not appeared")

    def select_destination(self, destination):
        self.find_element(By.ID, ':re:').send_keys(destination)
        time.sleep(1)
        self.find_element(By.ID, 'autocomplete-result-0').click()

    def select_dates(self, check_in, check_out):
        self.find_element(By.XPATH, f"//span[@data-date='{check_in}']").click()
        self.find_element(By.XPATH, f"//span[@data-date='{check_out}']").click()

    def select_occupancy(self, adults):
        if adults != 2:
            self.find_element(By.CLASS_NAME, "d777d2b248").click()
            value = int(self.find_element(By.ID, "group_adults").get_attribute("value"))
            # print(type(value))
            if adults > 2:
                while value != adults:
                    self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[2]').click()
                    value += 1
            if adults < 2:
                while value != adults:
                    self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[1]').click()
                    value -= 1

    def search_click(self):
        self.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def filters(self):
        filter = Filters(driver=self)
        #sleep temporary solution, change for expected condition: loaded page
        time.sleep(2)
        filter.star_rating(0, 1, 3)
