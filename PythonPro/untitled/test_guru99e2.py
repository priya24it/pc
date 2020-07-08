
import pytest
import request
import requests
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
from keyboard import press
import keyboard
import autoit


from Logfile.Commonclass import Commonclass
from PageObjects.HomePage import TestLinkMobile
#from selenium.webdriver.support.relative_locator  import  with_tag_name



@pytest.mark.usefixtures("setup")
class TestGuru99(Commonclass):

    @pytest.mark.skip
    def test_sort(self):
        log = Commonclass.getLogger(self)
        log.info("Started execution of TC001")

        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        TitleofmobilePage = mobilepage.getTitle()
        assert mobilepage.Title == TitleofmobilePage , "Pass"

        log.info("Title has matched , the requested  mobile page has opened  successfully...")
        l1 = mobilepage.listofelements()
        log.info("the list of elements..")
        log.info(l1)
        self.driver.execute_script("window.scrollBy(0,90)", "")
        self.driver.get_screenshot_as_file("TC001_sorybyname.png")
        log.info("Mobile Names has arranged ..... Screenshot has saved.")


    @pytest.mark.skip
    def test_sonyXperiaPrice(self):
        Parentprice = ""
        log = Commonclass.getLogger(self)
        log.info("Started execution of TC001")

        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        TitleofmobilePage = mobilepage.getTitle()
        time.sleep(3)
        #assert mobilepage.Title == TitleofmobilePage, "Pass"

        log.info("Title has matched , the requested  mobile page has opened  successfully...")
        ParentPrice = self.driver.find_element_by_xpath("//span[@id='product-price-1']//span").text
        log.info(ParentPrice)

        self.driver.find_element_by_partial_link_text("SONY XPERIA").click()
        time.sleep(3)

        Childprice = self.driver.find_element_by_css_selector("span.price").text
        log.info(Childprice)

        ParentPrice = ParentPrice[1:len(ParentPrice)-3]
        ParentPrice = int(ParentPrice)
        log.info(ParentPrice)

        Childprice = Childprice[1:len(Childprice) - 3]
        Childprice = int(Childprice)
        log.info(Childprice)

        assert ParentPrice ==Childprice , "Prices are not matching between the pages hence TC failed."







    @pytest.mark.skip
    def test_sonyXperiaaddtoCart(self):
        Parentprice = ""
        log = Commonclass.getLogger(self)
        log.info("Started execution of TC001")

        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        TitleofmobilePage = mobilepage.getTitle()
        time.sleep(3)
        # assert mobilepage.Title == TitleofmobilePage, "Pass"

        log.info("Title has matched , the requested  mobile page has opened  successfully...")
        self.driver.find_element_by_xpath("//a[contains(text(),'Sony Xperia')]//parent::h2//parent::div//button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//table[@id='shopping-cart-table']/tbody/tr/td[4]/input").clear()
        self.driver.find_element_by_xpath("//table[@id='shopping-cart-table']/tbody/tr/td[4]/input").send_keys(1000)
        self.driver.find_element_by_xpath("//table[@id='shopping-cart-table']/tbody/tr/td[4]/input").click()
        time.sleep(6)
       # errormessage = self.driver.find_element_by_xpath("//ul//li[@class='error-msg']//ul//li//span").text
       # print(errormessage)
        element = self.driver.find_element_by_xpath("//button[@id='empty_cart_button']")
        time.sleep(2)
        element.click()
        print(element)
        time.sleep(3)
       # self.driver.find_element_by_css_selector("h1").click()

    @pytest.mark.skip
    def test_compare(self):
        Parentprice = ""
        log = Commonclass.getLogger(self)
        log.info("Started execution of TC004")

        HomePageLinkMobile = TestLinkMobile(self.driver)
        mobilepage = HomePageLinkMobile.linkmobile()
        TitleofmobilePage = mobilepage.getTitle()
        time.sleep(3)
        # assert mobilepage.Title == TitleofmobilePage, "Pass"

        log.info("Title has matched , the requested  mobile page has opened  successfully...")
        self.driver.find_element_by_xpath("//a[contains(text(),'Sony Xperia')]//parent::h2//parent::div//a[contains(text(),'Add to Compare')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(),'IPhone')]//parent::h2//parent::div//a[contains(text(),'Add to Compare')]").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector("button[title='Compare']").click()
        #self.driver.find_element_by_xpath("//table[@id='shopping-cart-table']/tbody/tr/td[4]/input").click()
        childWindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childWindow)
        Text = self.driver.find_element_by_css_selector("h1").text
        print(Text)
        log.info(Text)
        self.driver.close()
        parentWindow = self.driver.window_handles[0]
        self.driver.switch_to.window(parentWindow)
        time.sleep(6)


    @pytest.mark.skip
    def test_accountcreation(self):
        log = Commonclass.getLogger(self)
        log.info("started")
        self.driver.find_element_by_link_text("ACCOUNT").click()
        self.driver.find_element_by_link_text("Register").click()
        time.sleep(2)
        i = random.randint(1,100)
        firstname = "irct"+str(i)
        lastname = "irct"+str(i)
        emailaddress = "irct"+str(i)+"@railways.com"


        self.driver.find_element_by_id("firstname").clear()
        self.driver.find_element_by_id("firstname").send_keys(firstname)
        self.driver.find_element_by_id("lastname").clear()
        self.driver.find_element_by_id("lastname").send_keys(lastname)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(emailaddress)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("Anusha@24")
        self.driver.find_element_by_id("confirmation").clear()
        self.driver.find_element_by_id("confirmation").send_keys("Anusha@24")
        self.driver.find_element_by_id("is_subscribed").click()
        self.driver.find_element_by_css_selector("button[title='Register']").click()
        time.sleep(2)
        ExceptedMessge = self.driver.find_element_by_xpath("//div[@class='welcome-msg']/p[1]").text
        ActualMessge = "Hello, " + firstname + " "+lastname+"!"
        log.info(ExceptedMessge)
        log.info(ActualMessge)
        assert ExceptedMessge == ActualMessge, "Both the messages are passed , hence it executes the next step in a sequence order"
       # self.driver.find_element_by_link_text(" My Account").click()
        self.driver.find_element_by_link_text("TV").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[contains(text(),'LG LCD')]//parent::h2//parent::div//a[contains(text(),'Add to Wishlist')]").click()
        self.driver.find_element_by_css_selector("button[name='save_and_share']").click()
        self.driver.find_element_by_id("email_address").clear()
        self.driver.find_element_by_id("email_address").send_keys("support@guru99.com")
        self.driver.find_element_by_css_selector("button[title='Share Wishlist']").click()
        successmessage = self.driver.find_element_by_xpath("//span[contains(text(),'Your Wishlist has been shared.')]").text
        Exceptedmessage = "Your Wishlist has been shared."
        time.sleep(2)
        assert successmessage == Exceptedmessage , "Both the messages are not same hence TC failed"

    @pytest.mark.skip
    def test_accountcreation(self):
        log = Commonclass.getLogger(self)
        log.info("started")
        self.driver.find_element_by_link_text("ACCOUNT").click()
        self.driver.find_element_by_link_text("Log In").click()
        time.sleep(1)
        emailaddress = "sbiindia@tame.com"
        password = "Anusha@24"
        self.driver.find_element_by_xpath("//input[@id='email']").clear()
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys(emailaddress)
        self.driver.find_element_by_id("pass").clear()
        self.driver.find_element_by_id("pass").send_keys(password)
        self.driver.find_element_by_css_selector("button[title='Login']").click()
        time.sleep(3)
        welcomemessage = self.driver.find_element_by_xpath("//div[@class='welcome-msg']//p[1]").text
        log.info(welcomemessage)

        self.driver.execute_script("window.scrollBy(0,120)", "")


        self.driver.find_element_by_link_text("MY WISHLIST").click()
        self.driver.find_element_by_css_selector("button[title='Add to Cart']").click()
        time.sleep(1)
        countryDropdown = Select(self.driver.find_element_by_id("country"))
        countryDropdown.select_by_visible_text("India")
        selectedvalue = countryDropdown.select_by_visible_text("India")
        log.info(selectedvalue)
        self.driver.find_element_by_id("region").clear()
        self.driver.find_element_by_id("region").send_keys("Telegana")
        self.driver.find_element_by_id("postcode").clear()
        self.driver.find_element_by_id("postcode").send_keys("50083")

        self.driver.find_element_by_css_selector("button[title='Estimate']").click()
        time.sleep(1)
        self.driver.find_element_by_name("estimate_method").click()
        self.driver.find_element_by_css_selector("button[title='Proceed to Checkout']").click()
        self.driver.execute_script("window.scrollBy(0,110)", "")



        self.driver.find_element_by_css_selector("button[title = 'Continue']").click()
        self.driver.execute_script("window.scrollBy(0,140)", "")
        time.sleep(2)

        self.driver.find_element_by_xpath("//*[@id='shipping-method-buttons-container']/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@title='Check / Money order']").click()
        self.driver.find_element_by_xpath("//*[@id='payment-buttons-container']/button").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,110)", "")
        self.driver.find_element_by_xpath("//*[@id='review-buttons-container']//button[@title='Place Order']").click()


        #self.driver.find_element_by_xpath("//*[@id='review-buttons-container']/button").click()
        time.sleep(2)
        expectedmessage = "YOUR ORDER HAS BEEN RECEIVED."
        actualmessage = "YOUR ORDER HAS BEEN RECEIVED."
        assert expectedmessage == expectedmessage , "Actual and Expected messages are differnt hence TC has failed."
        print(self.driver.find_element_by_css_selector("a[href*='view/order_id']").text)
        log.info(self.driver.find_element_by_css_selector("a[href*='view/order_id']").text)


    def test_saveasPDF(self):
        time.sleep(4)
        log = Commonclass.getLogger(self)
        log.info("started")
        self.driver.find_element_by_link_text("ACCOUNT").click()
        self.driver.find_element_by_link_text("Log In").click()
        time.sleep(1)
        emailaddress = "sbiindia@tame.com"
        password = "Anusha@24"
        self.driver.find_element_by_xpath("//input[@id='email']").clear()
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys(emailaddress)
        self.driver.find_element_by_id("pass").clear()
        self.driver.find_element_by_id("pass").send_keys(password)
        self.driver.find_element_by_css_selector("button[title='Login']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//table[@id='my-orders-table']//tr[1]//td[6]")
        numberofrows = self.driver.find_elements_by_xpath("//table[@id='my-orders-table']//tr")
        log.info(len(numberofrows))
        numberofcolumns = self.driver.find_elements_by_xpath("//table[@id='my-orders-table']//tr//td")
        log.info(len(numberofrows))
        rownum =1
        columnnum = 6
        xpath = "//table[@id='my-orders-table']//tr["+str(rownum)+"]//td["+str(columnnum)+"]"
        parentelement = self.driver.find_elements_by_xpath(xpath)
        log.info(parentelement)
        log.info(self.driver.title)
        orderNumber = "//table[@id='my-orders-table']//tr[1]//td[1]"
        orderNumber = self.driver.find_elements_by_xpath(orderNumber)
        log.info(orderNumber)

        for i in range(0,len(parentelement)):
            links = parentelement[i].text
            log.info(links)
            parentelement[i].find_element_by_link_text("VIEW ORDER").click()
            break
        time.sleep(1)
        self.driver.find_element_by_link_text("Print Order").click()
        childwindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childwindow)
        log.info(self.driver.title)

        time.sleep(1)
        self.driver.execute_script("window.print()", "")
        press('enter')
        time.sleep(3)
        autoit.win_activate("Save Print Output As")
        autoit.control_focus("Save Print Output As","")
        #autoit.control_focus()
        autoit.send("abc11")


        press('enter')
       # autoit.
       # alert = self.driver.switch_to.alert
       # alert.send_keys("abc")
        #alert.accept()

        #dropdown.select_by_visible_text("Save as PDF")

       # self.driver.find_element_by_css_selector("cr-button[class ='action-button']").click()
        time.sleep(1)
        logfile = r'abc.pdf'
        fileName = r"C://Users//PRIYA//Downloads//abc11.pdf"
        Commonclass.send_status(self,fileName)
        #self.driver.close()
        listofWindows = self.driver.window_handles
        log.info(len(listofWindows))
        window2 = self.driver.window_handles[1]
        self.driver.switch_to.window(window2)
        self.driver.close()
        parentwindow = self.driver.window_handles[0]
        self.driver.switch_to.window(parentwindow)

        #mail.send_status(logfile)













































































