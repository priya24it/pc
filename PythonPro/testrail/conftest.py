import pytest
from datetime import datetime
import pytest
from testrail_api import TestRailAPI
from utils import get_testrail_params

@pytest.fixture(scope="class")
def setup(request):
    global driver
    config = get_testrail_params()

    driver = TestRailAPI(config['url'], config['user_email'], config['user_key'])

    #driver.get("https://www.google.com")
    #driver.get("https://www.google.com")
    #driver.get("https://www.worldometers.info/geography/flags-of-the-world")
    #driver.get("https://www.guru99.com/handling-dynamic-selenium-webdriver.html")
    #driver.get("http://demo.guru99.com/test/web-table-element.php")
    #driver.find_elements_by_tag_name()
    request.cls.driver = driver
