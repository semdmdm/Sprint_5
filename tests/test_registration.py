import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

# все тесты советую запускать с впн, т.к. с ним гораздо быстрее это происходит, без впн - присутствует
# задержка секунд в 10-15 между открытием браузера (главной страницы сервиса) и запуском шагов теста внутри браузера
# Хотел добавить рандом чисел в генерирование email, но потом понял, что будет рандомить во всех места,
# а надо чтобы при регистрации и логине были одинаковые 3 цифры в email

class TestRegistration:

    def setup_method(self):  # Здесь использовал setup_method вместо конструктора __init__,
        # т.к. он более спокойно работет в связке с pytest по инф с хабра
        self.name = "Дмитрий"
        self.email = "Semenov_Dmitry_15_QA_FS_275@mail.ru"
        self.correct_password = "sd15qafs"
        self.incorrect_password = "sd"

    def test_registration_incorrect_password_error_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        driver.find_element(By.XPATH, Locators.NAME_INPUT_REGISTRATION).send_keys(self.name)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT_REGISTRATION).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT_REGISTRATION).send_keys(self.incorrect_password)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_REGISTER_PAGE).click()
        error = driver.find_element(By.XPATH, Locators.ERROR_MESSAGE).text
        assert error == "Некорректный пароль"
        driver.quit()

    def test_succesfull_registration_Chrome(self, driver):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        driver.find_element(By.XPATH, Locators.NAME_INPUT_REGISTRATION).send_keys(self.name)
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT_REGISTRATION).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT_REGISTRATION).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON_REGISTER_PAGE).click()
        time.sleep(2)   # Тут пришлось использовать sleep т.к. через WebDriverWait и expected_conditions вообще
        # никак не получается выдержать тайминг после нажатия кнопки "Зарегистрироваться", не помогают ни функции
        # ни по кликабельности ни по визуализации, вообще никак не смог (каждый раз после нажатия кнопки есть какая
        # задержка именно на кнопке "Зарегистрироваться", которая не дает потом на след странице
        # ввести email, прыгает через этот шаг. (работает только с импортированием time)
        # Осознаю (прочитал на хабре), что вариант с принудительной задержкой
        # - остановкой теста не самый лучший и опасный, но иначе не смог в данном случае.
        # Спецом сделал заготовки по visibility и clickable и оставил импорты в шапке
        # WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.EMAIL_INPUT)))
        # WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.EMAIL_INPUT)))
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(self.correct_password)
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'
        driver.quit()
