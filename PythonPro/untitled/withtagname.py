import pytest
import requests
import request
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import  selenium.webdriver.support.relative_locator as RelativeLocator
from webdriver_manager.driver import ChromeDriver


driver =  webdriver.Chrome(executable_path="C://Python Pro//untitled//CromeDriver//chromedriver.exe")



driver.get("http://live.demoguru99.com/index.php/")
driver.find_element_by_link_text("MOBILE").click()
time.sleep(4)
driver.close()
