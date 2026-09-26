def test_successful_registration(create_new_account):
    assert (
        create_new_account.get_success_message()
        == "Your account was created successfully. You are now logged in."
    )