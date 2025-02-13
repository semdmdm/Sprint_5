import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()    # на всякий случай делаем окно на всю, чтобы заодно
    # проверить роботоспособность в рабочем разрешени десктопа
    driver.get("https://stellarburgers.nomoreparties.site/")    # все тесты будут стартовать только с главной страницы
    # сайта, для дополнительной проверки переходов и возможности выявления дополнительных багов при их наличии
    return driver