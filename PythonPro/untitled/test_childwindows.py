import pytest
import request
import requests
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
@pytest.mark.skip
class TestChildWindows:
    def test_childwindows(self):
        print("statred")
        element = self.driver.find_element_by_xpath("//ul[1]/li[2]")
        time.sleep(5)
        print("statred123.....")
        links = element.find_elements_by_xpath("//ul[1]//li[1]//a[contains(@class,'elementor-sub-item')][contains(text(),'Manual Testing')]")
        print(links)
        s = ()
        l1 = []
        for link in range(0, len(links)):
            url = links[link].get_attribute('href')
            l1.append(url)
            status = requests.head(url)
            response = status.status_code

        s = set(l1)
        print(s)
        l1 = list(s)
        print(l1[0])
        self.driver.get(l1[0])
        time.sleep(4)
        print(self.driver.current_url)
        time.sleep(8)

        childwindow = self.driver.window_handles
        print("length of the "+str(len(childwindow)))

        self.driver.switch_to_window(childwindow[0])

        wait = WebDriverWait(self.driver,20)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//ul[2]//li[1]//a[1][contains(text(),'Software Testing')]")))
        element1 = self.driver.find_element_by_xpath("//ul[2]//li[1]//a[1][contains(text(),'Software Testing')]")
        print(element1.get_attribute('href'))
        element1 = element1.get_attribute('href')
        self.driver.get(element1)
        time.sleep(8)
        #element2 = self.driver.find_element_by_xpath("//ul[2]/li[2]").click()
        #time.sleep(4)
        #element3 = self.driver.find_element_by_xpath("//ul[2]/li[4]").click()


