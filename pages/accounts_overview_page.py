from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountsOverviewPage(BasePage):

    ACCOUNTS_OVERVIEW_MENU_LINK = (By.LINK_TEXT, "Accounts Overview")
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href*='activity.htm']")

    def open_via_menu(self):
        self.click(self.ACCOUNTS_OVERVIEW_MENU_LINK)

    def get_account_id(self):
        return self.find(self.ACCOUNT_LINK).text
