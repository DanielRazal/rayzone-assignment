from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FindTransactionsPage(BasePage):

    FIND_TRANSACTIONS_MENU_LINK = (By.LINK_TEXT, "Find Transactions")
    DATE_INPUT = (By.ID, "transactionDate")
    FIND_BY_DATE_BUTTON = (By.ID, "findByDate")
    RESULTS_ROWS = (By.CSS_SELECTOR, "#transactionBody tr")

    def open_via_menu(self):
        self.click(self.FIND_TRANSACTIONS_MENU_LINK)

    def find_by_date(self, date_str):
        self.type(self.DATE_INPUT, date_str)
        self.click(self.FIND_BY_DATE_BUTTON)

    def get_results_text(self):
        rows = self.find_all(self.RESULTS_ROWS)
        return [row.text for row in rows]
