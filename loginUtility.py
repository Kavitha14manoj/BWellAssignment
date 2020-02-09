from PageObjects import loginPage

def login(driver,accountName,emailAddress,password):
    driver.implicitly_wait(30)
    driver.find_element_by_id(loginPage.appNameTextField).send_keys(accountName)
    driver.find_element_by_id(loginPage.emailAddressTextField).send_keys(emailAddress)
    driver.find_element_by_id(loginPage.pwdTextField).send_keys(password)
    driver.find_element_by_id(loginPage.submitButton).click()


