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

class TestGuru99:
    def test_partialinktest(self):
        print("statred")
        tutoiral = self.driver.find_element_by_xpath("//ul/li[2]")
        actions = ActionChains(self.driver)
        actions.move_to_element(tutoiral).click().perform()
        time.sleep(2)

        elements = self.driver.find_elements_by_partial_link_text("//ul//li[2]//ul[1][@class='sub-menu elementor-nav-menu--dropdown sm-nowrap']")
        print(elements)

