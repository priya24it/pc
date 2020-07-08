import pytest
import request
import requests
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.skip
class ManualTestingTutorials:

    def __init__(self,driver):
        self.driver = driver

    def openWebPage(self,url):
        self.driver.get(url)

    def clickonSoftwareTestingLink(self):
        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//ul[2]//li[1]//a[1]")))
        element = self.driver.find_elements_by_xpath("//ul[2]//li[1]//a[1]")



