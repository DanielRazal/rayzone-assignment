import os

import requests
from dotenv import load_dotenv
from pages.accounts_overview_page import AccountsOverviewPage

load_dotenv()


def test_transfer_and_validate(registered_user):
    driver = registered_user
    base_url = os.getenv("BASE_URL")

    accounts_overview_page = AccountsOverviewPage(driver)
    accounts_overview_page.open_via_menu()
    account_id = accounts_overview_page.get_account_id()
    balance = accounts_overview_page.get_balance()
    transfer_amount = round(balance / 3, 2)

    session = requests.Session()
    for cookie in driver.get_cookies():
        session.cookies.set(cookie["name"], cookie["value"])

    transfer_response = session.post(
        f"{base_url}/services_proxy/bank/transfer",
        params={
            "fromAccountId": account_id,
            "toAccountId": account_id,
            "amount": transfer_amount,
        },
    )

    assert transfer_response.status_code == 200
    assert (
        transfer_response.text
        == f"Successfully transferred ${transfer_amount:.2f} from account #{account_id} to account #{account_id}"
    )
