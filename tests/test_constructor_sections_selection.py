import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestConstructorSections:

    def test_constructor_buns_button_Chrome(self, driver, data):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT)))   # Выставлен тайм-аут, т.к. проверки 50/50 без тайминга проходят с ошибкой, не успевает форма загрузиться
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["correct_password"])
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()   # Здесь единственный случай, где необходимо инициализировать # переключение на сторонний раздел "Соусы", т.к. страница изначально открывается на разделе "Булки"
        driver.find_element(By.XPATH, Locators.BUNS_BUTTON).click()   
        selected_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SELECTED_SECTION_SPAN).text   # Создаем переменную, которая   # содержит текст дочернего span выбранного раздела   # Локатор CONSTRUCTOR_SELECTED_SECTION_SPAN содержит код !!ИМЕННО ВЫБРАННОГО РАЗДЕЛА!! "tab_tab_type_current__2BEPc" именно при выборе раздела
        assert selected_section == "Булки"

    def test_constructor_sauces_button_Chrome(self, driver, data):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["correct_password"])
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_BUTTON).click()
        selected_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SELECTED_SECTION_SPAN).text
        assert selected_section == "Соусы"

    def test_constructor_fillings_button_Chrome(self, driver, data):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["correct_password"])
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.XPATH, Locators.FILLINGS_BUTTON).click()
        selected_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SELECTED_SECTION_SPAN).text
        assert selected_section == "Начинки"
