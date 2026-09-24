from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):
    
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[value='Register']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#rightPanel p")


    def register(self, first_name, last_name, address, city, state,
                    zip_code, phone, ssn, username, password):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.ADDRESS, address)
        self.type(self.CITY, city)
        self.type(self.STATE, state)
        self.type(self.ZIP_CODE, zip_code)
        self.type(self.PHONE, phone)
        self.type(self.SSN, ssn)
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)
        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
            WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element(self.SUCCESS_MESSAGE, "successfully")
            )
            return self.find(self.SUCCESS_MESSAGE).text