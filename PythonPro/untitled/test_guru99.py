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
       # element = self.driver.find_element_by_partial_link_text("//ul[@id='menu-1-9725c2b']/li[2]//a[contains(text(),'Tutorials')]")
       # element.click()

        elements = self.driver.find_element_by_partial_link_text("Tutorials")
        print(elements)


        #elements.click()
        #elements.find_element_by_partial_link_text("Manual Testing")
        #time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(elements).click().perform()
        time.sleep(1)
        element = self.driver.find_element_by_partial_link_text("Manual Testing")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)

        elements = self.driver.find_element_by_partial_link_text("//p[@class='elementor-heading-title elementor-size-default']")
        print(elements)
        actions = ActionChains(self.driver)
        actions.move_to_element(elements).click().perform()
        time.sleep(1)
        element = self.driver.find_element_by_partial_link_text("Java")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)

        elements = self.driver.find_element_by_partial_link_text("Tutorials")
        print(elements)
        actions = ActionChains(self.driver)
        actions.move_to_element(elements).click().perform()
        time.sleep(1)
        element = self.driver.find_element_by_partial_link_text("Framework")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)


        elements = self.driver.find_element_by_partial_link_text("Tutorials")
        print(elements)
        actions = ActionChains(self.driver)
        actions.move_to_element(elements).click().perform()
        time.sleep(1)
        element = self.driver.find_element_by_partial_link_text("Agile")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        time.sleep(2)















