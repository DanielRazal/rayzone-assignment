import os
import random
from dotenv import load_dotenv
from pages.registration_page import RegistrationPage
from pages.home_page import HomePage

load_dotenv()


def test_successful_registration(driver):
    base_url = os.getenv("BASE_URL")
    base_username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")
    username = f"{base_username}{random.randint(1000, 9999)}"

    driver.get(f"{base_url}/index.htm")

    home_page = HomePage(driver)
    home_page.click_register()

    registration_page = RegistrationPage(driver)
    registration_page.register(
        first_name="Daniel",
        last_name="Razal",
        address="123 Main St",
        city="Tel Aviv",
        state="TA",
        zip_code="12345",
        phone="0501234567",
        ssn="918273645",
        username=username,
        password=password,
    )

    assert (
        registration_page.get_success_message()
        == "Your account was created successfully. You are now logged in."
    )