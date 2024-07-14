import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from data import UsersTestData
from conftest import driver, login

# Вход по кнопке «Войти в аккаунт» на главной странице
class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed()

        # Вход через кнопку "Личный кабинет":
    def test_login_from_personal_account_button(self, driver, login):
            driver.get("https://stellarburgers.nomoreparties.site/")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_personal_account)).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(login.email)
            driver.find_element(*TestLocators.input_password_auth).send_keys(login.password)
            driver.find_element(*TestLocators.button_login).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
            assert driver.find_element(*TestLocators.button_make_the_order).is_displayed()

            # вход через кнопку в форме регистрации

    def test_authentication_by_button_login_in_registration_form_success(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_register)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_registration_form)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed()

        # вход через кнопку в форме восстановления пароля.

    def test_login_from_password_recovery_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_passwd_recovery_form)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(UsersTestData.email)
        driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*TestLocators.button_login).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
        assert driver.find_element(*TestLocators.button_make_the_order).is_displayed()