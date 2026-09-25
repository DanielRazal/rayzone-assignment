from conftest import create_new_account


def test_successful_registration(driver):
    registration_page = create_new_account(driver)

    assert (
        registration_page.get_success_message()
        == "Your account was created successfully. You are now logged in."
    )