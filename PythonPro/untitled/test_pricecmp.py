import pytest
import time
import UtilityClass.UC as uc

@pytest.mark.usefixtures("setup")
@pytest.mark.skip
class TestComparison(uc.Utility):

    def test_compare(self):
        print("window opened successfully... ")
        time.sleep(4)
        bestprice = self.driver.find_element_by_xpath("//span[@class='prdct-dtl__prc-val']").text

        l1 = bestprice.split(',')
        for i in range(0, len(l1)):
            print(l1[i])
            bestprice = l1[0] + l1[1]
        #print(bestprice)

        print("best price is" + bestprice)
        l1  = []
        j = 0

        dtastore = self.driver.find_element_by_xpath("//div[@class='prdct-dtl__cntr']//div[1]").get_attribute('data - storename')
        #print(dtastore)
        dict = {}
        store = ""


        for i in range(1,5):
            CurrentURl = self.driver.find_element_by_xpath("//div[@class='prdct-dtl__cntr']//div["+str(i)+"]//div[1]//div[3]//a[1]").get_attribute('href')
            #print(CurrentURl)
            l2 =str(CurrentURl).split('&')
            #print(l2[6])
            dict[l2[6]] = [CurrentURl]
            l1.insert(j,CurrentURl)
            j = j+1

        print(dict)
        for i in range(0, len(l1)):
            print(i)
            #print(l1[i])
            #print("loop variable" + str(i))
            WebsitePrice = uc.Utility(self.driver, l1[i], str(i))
            websiteprice = WebsitePrice.getwebsiteprice()
                # assert bestprice == websiteprice, "testcase passed"


            #for i in range(0,len(l2)):
                #print(l2[i])
                #for l2 in "store=":
                    #print(l2)




        time.sleep(2)






