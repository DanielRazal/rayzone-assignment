import requests


def build_authenticated_session(driver):
    session = requests.Session()
    for cookie in driver.get_cookies():
        session.cookies.set(cookie["name"], cookie["value"])
    return session


def transfer_funds(session, base_url, account_id, amount):
    return session.post(
        f"{base_url}/services_proxy/bank/transfer",
        params={
            "fromAccountId": account_id,
            "toAccountId": account_id,
            "amount": amount,
        },
    )


def find_transactions_by_date(session, base_url, account_id, date_str):
    return session.get(
        f"{base_url}/services_proxy/bank/accounts/{account_id}/transactions/onDate/{date_str}"
    )
