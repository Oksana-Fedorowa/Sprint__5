import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from data import UsersTestData
from constants import BASE_URL

@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def login():
    return UsersTestData

@pytest.fixture(scope="function")
def logged_in_driver(driver, login):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(login.email)
    driver.find_element(*TestLocators.input_password_auth).send_keys(login.password)
    driver.find_element(*TestLocators.button_login).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
    yield driver