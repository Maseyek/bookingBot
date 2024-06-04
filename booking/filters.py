from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class filters:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_rating(self):
        self.driver.find_element(By.XPATH, '//*[@id="filter_group_class_:r18:"]/div[5]/label/span[2]').click()






