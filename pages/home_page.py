from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    REGISTER_LINK = (By.LINK_TEXT, "Register")

    def click_register(self):
        self.click(self.REGISTER_LINK)
