import pytest
import requests
import request
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.driver import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
import os


chromedriver =ChromeDriverManager().install()
download_dir = "C:\\Users\\omprakashpk\\Documents" # for linux/*nix, download_dir="/usr/Public"
options = webdriver.ChromeOptions()

profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(chromedriver, chrome_options=options)  # Optional argument, if not specified will search path.

