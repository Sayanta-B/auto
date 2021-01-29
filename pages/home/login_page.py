from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    #locaters
    _login_link='//a[@href="/login"]'
    _email_field='//div[@class="form-group"]//input[contains(@type,"email") and contains(@tabindex,"4")]'
    _password_field='//*[@id="password"]'
    _login_button='/html/body/div[1]/div[2]/div/div/div/div/form/div[4]/div[1]/input'

    def getLoginLink(self):
        return self.driver.find_element_by_xpath(self._login_link)
    def getEmailField(self):
        return self.driver.find_element_by_xpath(self._email_field)
    def getPasswordField(self):
        return self.driver.find_element_by_xpath(self._password_field)
    def getLoginButton(self):
        return self.driver.find_element_by_xpath(self._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()
    def enterEmail(self,email):
        self.getEmailField().send_keys(email)
    def enterPassword(self,password):
        self.getPasswordField().send_keys(password)
    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
