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


@pytest.fixture(scope="class")
def setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument("--disable-print-preview");
    #options.add_experimental_option("download.extensions_to_open":application/pdf)
    #options.add_argument("download.extensions_to_open": "application/pdf")

    cap = DesiredCapabilities.CHROME
    #cap["download.default_directory"] = "C:"
   # cap["download.prompt_for_download"] = "false"
   # cap["directory_upgrade"] == "true"
   # cap["plugins.plugins_disabled"]== "Chrome PDF Viewer"
    #capa["pageLoadStrategy"] = "none"

    #prefs = {'profile.default_content_setting_values.notifications': 2}
    #options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options,desired_capabilities=cap)

    #driver = webdriver.Chrome(executable_path="C://Python Pro//untitled//CromeDriver//chromedriver.exe",chrome_options=options,desired_capabilities=capa)

   # driver.get("https://www.mysmartprice.com/mobile/apple-iphone-7-msp10208")
    #driver.get("https://www.softwaretestingmaterial.com/")
    #driver.get("http://live.demoguru99.com/index.php/")
    driver.get("https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/icicibank/ICI02")
    request.cls.driver = driver

    #driver.switch_to.window()
    #driver.get_screenshot_as_png()



    driver.maximize_window()
    #capabilities = DesiredCapabilities.CHROME.copy()
    #  webdriver.DesiredCapabilities.CHROME.copy()
    #  webdriver.ChromeOptions()
    yield
    driver.close()




@pytest.fixture(params = [(1,2),(3,4)])
def addidtion(request):
    return request.param





