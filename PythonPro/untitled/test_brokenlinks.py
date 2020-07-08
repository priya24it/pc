import pytest
import request
import requests
import pandas as pd
import time
@pytest.mark.usefixtures("setup")
@pytest.mark.skip
class TestBrokenLinks:
    d = {}
    def test_broken(self):
        print("statred")
        element = self.driver.find_element_by_xpath("//ul[1]/li[2]")
        time.sleep(5)
        links = element.find_elements_by_tag_name("a")  # .get_attribute('href')
        # print(addidtion[0]+addidtion[1])
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
        # //a[@id='sm-15884780267433933-1']


