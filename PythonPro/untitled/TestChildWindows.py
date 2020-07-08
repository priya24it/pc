import pytest
import request
import requests
import time
import pandas as pd

@pytest.mark.usefixtures("setup")
class TestChildWindows:
    def test_childwindows(self):
        print("statred")
        element = self.driver.find_element_by_xpath("//ul[1]/li[2]")
        time.sleep(5)
        links = element.find_elements_by_tag_name("ul[1]//li[1]//a[contains(@class,'elementor-sub-item')][contains(text(),'Manual Testing')]")
        for link in range(0, len(links)):
            url = links[link].get_attribute('href')
            status = requests.head(url)
            response = status.status_code

            self.d[url] = response
            print(type(self.d))
        df = pd.DataFrame(self.d,index=['statuscode'])
        print(df)
        df = df.T
        df.to_excel("links.xlsx")


        #element1 = self.driver.find_element_by_xpath("//ul[2]/li[1]").click()
        #element2 = self.driver.find_element_by_xpath("//ul[2]/li[2]").click()
        #element3 = self.driver.find_element_by_xpath("//ul[2]/li[4]").click()


