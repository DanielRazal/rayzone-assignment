import os
from datetime import date, datetime

from dotenv import load_dotenv
from pages.accounts_overview_page import AccountsOverviewPage
from tests.api_helpers import (
    build_authenticated_session,
    find_transactions_by_date,
    transfer_funds,
)

load_dotenv()


def test_transfer_and_validate(registered_user):
    driver = registered_user
    base_url = os.getenv("BASE_URL")

    accounts_overview_page = AccountsOverviewPage(driver)
    accounts_overview_page.open_via_menu()
    account_id = accounts_overview_page.get_account_id()
    balance = accounts_overview_page.get_balance()
    transfer_amount = round(balance / 3, 2)

    session = build_authenticated_session(driver)

    transfer_response = transfer_funds(session, base_url, account_id, transfer_amount)

    assert transfer_response.status_code == 200
    assert (
        transfer_response.text
        == f"Successfully transferred ${transfer_amount:.2f} from account #{account_id} to account #{account_id}"
    )

    today = date.today().strftime("%m-%d-%Y")
    find_response = find_transactions_by_date(session, base_url, account_id, today)

    assert find_response.status_code == 200

    transactions = find_response.json()
    transaction = transactions[0]

    assert transaction["accountId"] == int(account_id)
    assert transaction["amount"] == transfer_amount
    assert transaction["description"] in ("Funds Transfer Sent", "Funds Transfer Received")
    assert transaction["type"] in ("Debit", "Credit")
    assert isinstance(transaction["id"], int)

    transaction_date = datetime.fromtimestamp(transaction["date"] / 1000).date()
    assert transaction_date == date.today()