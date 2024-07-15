
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, login
from constants import BASE_URL

class TestNavigation:
    def test_navigation_from_personal_account_to_constructor(self, driver, login):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(login.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(login.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_personal_account)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.profile))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.header_of_page_constructor)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed()

    def test_navigation_from_logo(self, driver, login):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(login.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(login.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_personal_account)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.profile))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.logo)).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed()