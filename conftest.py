import os
import random

import pytest
from dotenv import load_dotenv
from selenium import webdriver

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

load_dotenv()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def create_new_account(driver):
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
    return registration_page


@pytest.fixture
def registered_user(driver, create_new_account):
    create_new_account.get_success_message()
    return driver
