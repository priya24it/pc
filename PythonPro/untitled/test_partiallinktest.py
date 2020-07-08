import pytest
import request
import requests
import time
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
@pytest.mark.skip
class TestGuru99:
    def test_partialinktest(self):
        print("statred")
        tutoiral = self.driver.find_element_by_xpath("//ul/li[2]")
        actions = ActionChains(self.driver)
        actions.move_to_element(tutoiral).click().perform()
        time.sleep(2)

        elements = self.driver.find_elements_by_xpath("//ul//li[2]//ul[1][@class='sub-menu elementor-nav-menu--dropdown sm-nowrap']//li")
        print(len(elements))
        l1 = []

        for i in range(0,len(elements)):
            l1.insert(i,elements[i].text)
        #l1 = l1.sort()
        del l1[5]
        del l1[4]
        del l1[3]
        del l1[2]
        print(l1)

        for i in range(0,len(l1)):
            text = l1[i]
            print(text)
            elements = self.driver.find_element_by_partial_link_text("Tutorials")
            actions = ActionChains(self.driver)
            actions.move_to_element(elements).perform()
            time.sleep(1)

            element = self.driver.find_element_by_partial_link_text(text)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            self.driver.execute_script("window.scrollBy(0,100)","")

            time.sleep(4)
            ptag = self.driver.find_element_by_xpath(
                "//p[@class='elementor-heading-title elementor-size-default']")
            actions.move_to_element(ptag).perform()









