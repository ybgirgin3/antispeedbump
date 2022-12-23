from typing import Optional


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class Post:
    # driver
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'chromedriver'))
    driver.get('https://www.instagram.com/')
    by = {
        "id"    : By.ID,
        "name"  : By.NAME,
        "xpath" : By.XPATH,
        "css"   : By.CSS_SELECTOR
    }
    keys = {
        "enter" : Keys.ENTER
    }

    # fields
    # TODO: make them read from external file
    id_field = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
    pass_field = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"


    def __init__(self, image: dict):
        self.image = image


    def prepare(self):
        # login
        self.login()
        pass


    def login(self):
        username = self._find_element('xpath', self.id_field)


        

    def _find_element(self, property: str, string: str):
        return self.driver.find_element(self.by[property], string)

    def _send_keys(self, element:  etext: Optional[str] = None, key: Optional[str] = None):
        return 












    def process(self):
        imp = self.image['path']
        desc = self.image['description']

        return imp, desc
