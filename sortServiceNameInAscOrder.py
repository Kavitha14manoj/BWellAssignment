import unittest
from selenium import webdriver
from Utility import loginUtility,loginCredentials
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from builtins import sorted
from PageObjects import homePage

class signIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/Users/manoj.narayan/Documents/workspace/geckodriver")
    def test_signIn(self):
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("http://login.myappcms.com/")
        print(driver.current_url)
        self.assertIn("http://login.myappcms.com/", driver.current_url)
        
        loginUtility.login(driver,loginCredentials.accountName,loginCredentials.emailAddress,loginCredentials.password)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,homePage.mainTitleCss)))
        print(driver.current_url)
        
        driver.find_element_by_id(homePage.appoinmentMenuItemId).click()
        wait.until(EC.element_to_be_clickable((By.ID,homePage.serviceMenuItemId)))
        driver.find_element_by_id(homePage.serviceMenuItemId).click()
        wait.until(EC.presence_of_element_located((By.ID,homePage.tableGridViewId)))        
        numberOfRows= driver.find_elements_by_xpath(homePage.numberOfRowsXpath)
        print(len(numberOfRows))
        
        driver.find_element_by_id(homePage.serviceNameHeaderId).click()
        driver.find_element_by_id(homePage.serviceNameTriggerHeaderId).click()
        driver.find_element_by_id(homePage.ascOrderMenuItemId).click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,homePage.serviceNameColoumListCss))) 
        
        nameList=[]
        nameList.extend(elem.text for elem in driver.find_elements_by_css_selector(homePage.serviceNameColoumListCss))
        print(nameList)
        assert nameList == sorted(nameList)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()