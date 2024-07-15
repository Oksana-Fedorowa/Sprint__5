
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver
from helpers import create_random_email, create_random_password
from data import UsersTestData
from constants import REGISTER_URL


class TestRegistration:
#успешная регистрация
    def test_registration_new_account_success_submit(self, driver):

        random_email = create_random_email()
        random_password = create_random_password(8)
        driver.get(REGISTER_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_registration_form)).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_register))

        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_submit))

        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(random_email)
        driver.find_element(*TestLocators.input_password).send_keys(random_password)

        driver.find_element(*TestLocators.button_submit).click()

        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(TestLocators.button_login))

        assert driver.find_element(*TestLocators.button_login).is_displayed()


    def test_registration_with_invalid_password(self,driver):
         driver.get(REGISTER_URL)
         driver.find_element(*TestLocators.input_name).send_keys("Oksana")
         driver.find_element(*TestLocators.input_email).send_keys("oksana_fedorowa_11_004ya.ru")
         driver.find_element(*TestLocators.input_password).send_keys("123")
         driver.find_element(*TestLocators.button_submit).click()

         error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.notification_incorrect_password))

         assert error_message.text == "Некорректный пароль"


