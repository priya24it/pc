import pytest
import request
import requests
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Logfile.Commonclass import Commonclass


@pytest.mark.usefixtures("setup")
class MobilePage:
    driver = None

    teamElement = (By.CSS_SELECTOR, "select[title='Sort By']")
    listofnames = (By.XPATH, "//ul//li//div[1]//h2")
    Title = "Mobile"


    def __init__(self, driver):
        self.driver = driver



    def hello(self):
        print("hello..")

    def getteamElement(self):
        return self.driver.find_element(*MobilePage.teamElement)

    def getlistofnames(self):
        return self.driver.find_elements(*MobilePage.listofnames)

    def listofelements(self):
        time.sleep(2)
        teamElement = MobilePage.getteamElement(self)
       # print(teamElement)
        # teamElement = MobilePage.teamElement
        time.sleep(2)
        s = Select(teamElement)
        time.sleep(3)

        s.select_by_index(1)
        elements = MobilePage.getlistofnames(self)
        l1 = []
        print(len(elements))

        for i in range(0, len(elements)):
            print(elements[i].text)
            l1.insert(i, elements[i].text)

        return l1

    def getTitle(self):
        #log = Commonclass.getLogger()
        #log.info("Fetching the Title of a page")
        return self.driver.title

