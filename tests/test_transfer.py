from pages.accounts_overview_page import AccountsOverviewPage


def test_transfer_and_validate(registered_user):
    driver = registered_user

    accounts_overview_page = AccountsOverviewPage(driver)
    accounts_overview_page.open_via_menu()
    account_id = accounts_overview_page.get_account_id()
