import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from constants import BASE_URL
from conftest import logged_in_driver, driver, login

def test_logout_from_personal_account(logged_in_driver):
    driver = logged_in_driver
    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_personal_account)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.profile))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_logout)).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login))
    assert driver.find_element(*TestLocators.button_login).is_displayed()