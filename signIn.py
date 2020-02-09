import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PageObjects import loginPage,homePage

class signIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/Users/manoj.narayan/Documents/workspace/geckodriver")

    def test_signIn(self):
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get("http://login.myappcms.com/")
        print(driver.current_url)
        self.assertIn("http://login.myappcms.com/", driver.current_url)
        driver.find_element_by_id(loginPage.appNameTextField).send_keys("CMS Demo Account")
        driver.find_element_by_id(loginPage.emailAddressTextField).send_keys("demo@diyappdesigner.com")
        driver.find_element_by_id(loginPage.pwdTextField).send_keys("demo123")
        driver.find_element_by_id(loginPage.submitButton).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,homePage.mainTitleCss)))
        myAccount=driver.find_element_by_xpath(homePage.demoAccountNamexpath)
        myAccount.is_displayed()
        self.assertIn("http://login.myappcms.com/build", driver.current_url)
        print(driver.current_url)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()