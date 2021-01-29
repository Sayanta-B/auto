from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import  unittest
class LoginTests(unittest.TestCase):
    def test_validLogin(self):
        baseURL="https://courses.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        driver.implicitly_wait(3)

        lp=LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon=driver.find_element_by_xpath('//img[contains(@class,"zl-navbar-rhs-img")]')
        if userIcon is not None:
            print("Log in successfull")
        else:
            print("Login Unsuccessfull")
# ff=LoginTests()
# ff.test_validLogin()