import time

class Utility:
    childprice = ''
    childprice

    def __init__(self,driver,websiteURL,loopvariable):
        self.driver = driver
        self.url = websiteURL
        self.loopvariable = loopvariable


    def getwebsiteprice(self):
        print(self.url)
        print("loop variable" + str(self.loopvariable))
        if  str(self.loopvariable) == "0" :
           self.driver.get(self.url)
           time.sleep(5)
           childprice = self.driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
           childprice = childprice[1:len(childprice)]
           l1 = childprice.split(',')
           for i in range(0, len(l1)):
               print(l1[i])
           childprice = l1[0] + l1[1]
           print(childprice)
           print("child price" + str(childprice))
           childprice = int(childprice)


        elif str(self.loopvariable) == "1":
            self.driver.get(self.url)
            time.sleep(5)
            childprice = self.driver.find_element_by_xpath("//span[@class='_1V3w']").text
            childprice = childprice[1:len(childprice)]
            l1 = childprice.split(',')
            for i in range(0, len(l1)):
                print(l1[i])
            childprice = l1[0] + l1[1]
            print(childprice)
            print("child price" + str(childprice))
            childprice = int(childprice)

        elif str(self.loopvariable) == "2":
            self.driver.get(self.url)
            time.sleep(5)
            childprice = self.driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']").text
            childprice = childprice[1:len(childprice)]
            l1 = childprice.split(',')
            for i in range(0, len(l1)):
                print(l1[i])
            childprice = l1[0] + l1[1]
            print(childprice)
            print("child price" + str(childprice))
            childprice = int(childprice)

        else:
            self.driver.get(self.url)
            time.sleep(5)
            childprice = self.driver.find_element_by_xpath("//div[@class='e404_text']").text
            childprice = childprice[1:len(childprice)]
            l1 = childprice.split(',')
            if len(l1) > 1:
                for i in range(0, len(l1)):
                    print(l1[i])
                childprice = l1[0] + l1[1]
                print(childprice)
                print("child price" + str(childprice))
                childprice = int(childprice)
            else:
                childprice = 0

        return childprice






