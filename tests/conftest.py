import pytest
import random
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def data():
    return {"name" : "Дмитрий",
            "email_random": f"Semenov_Dmitry_15_QA_FS_{random.randint(100, 999)}@mail.ru",
            "email": f"Semenov_Dmitry_15_QA_FS_276@mail.ru",
            "correct_password": "sd15qafs",
            "incorrect_password": "sd"}





