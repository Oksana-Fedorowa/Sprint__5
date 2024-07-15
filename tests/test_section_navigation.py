import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, login
from constants import BASE_URL

def login_to_site(driver, login):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.button_login_in_main)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.input_email_auth)).send_keys(login.email)
    driver.find_element(*TestLocators.input_password_auth).send_keys(login.password)
    driver.find_element(*TestLocators.button_login).click()

def test_navigate_to_sauces_block(driver, login):
    driver.get(BASE_URL)
    login_to_site(driver, login)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.sauces_block)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))
    selected_section_text = driver.find_element(*TestLocators.selected_button).text
    assert selected_section_text == "Соусы"

def test_navigate_to_buns_block(driver, login):
    driver.get("https://stellarburgers.nomoreparties.site/")
    login_to_site(driver, login)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.sauces_block)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.buns_block)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))
    assert driver.find_element(*TestLocators.selected_button).text == "Булки"

def test_navigate_to_fillings_block(driver, login):
    driver.get(BASE_URL)
    login_to_site(driver, login)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.sauces_block)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.buns_block)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.fillings_block)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.selected_button))
    assert driver.find_element(*TestLocators.selected_button).text == "Начинки"
