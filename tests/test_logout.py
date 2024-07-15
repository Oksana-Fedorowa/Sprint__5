import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, login
from constants import BASE_URL

def test_logout_from_personal_account(driver, login):
    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(login.email)
    driver.find_element(*TestLocators.input_password_auth).send_keys(login.password)
    driver.find_element(*TestLocators.button_login).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_personal_account)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.profile))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_logout)).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login))
    assert driver.find_element(*TestLocators.button_login).is_displayed()