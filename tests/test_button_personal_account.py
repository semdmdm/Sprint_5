import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestMoveToPersonalAccount:

    def test_button_personal_account_Chrome(self, driver, data):
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT)))   # Выставлен тайм-аут, т.к. проверки 50/50 без тайминга проходят с ошибкой, не успевает форма загрузиться
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["correct_password"])
        driver.find_element(By.XPATH, Locators.ENTER_BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'   # Проверяем, что следствием всех действий
        # будет конечный переход на url, соответствующий странице аккаунта/профиля,
        # при переходе на данный url потом еще догружается автоматически /profile, но selenium останавливается на просто /account
