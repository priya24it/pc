import pytest
import request
import requests
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObjects.MobilePage import MobilePage
from Logfile.Commonclass import Commonclass


@pytest.mark.usefixtures("setup")
class TestLinkMobile:
    driver = None

    Mobile = (By.LINK_TEXT ,"MOBILE")


    def __init__(self,driver):
        self.driver=driver


    def linkmobile(self):
        #log = Commonclass.getLogger(self)
        #log.info("Click on the Mobile Link")
        self.driver.find_element(*TestLinkMobile.Mobile).click()
        mobilepage = MobilePage(self.driver)
        return mobilepage




