class Locators:
    ENTER_BUTTON_MAIN_PAGE = ".//button[text()='Войти в аккаунт']"   # Кнопка "Войти в аккаунт" на главной странице (XPATH)
    ENTER_BUTTON_PERSONAL_ACCOUNT = ".//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти')]"   # Кнопка "Войти" в форме авторизации (XPATH)
    ENTER_BUTTON_REGISTRATION_FORM = ".//a[@class='Auth_link__1fOlj' and @href='/login']"   # Кнопка "Войти" в форме регистрации (XPATH)
    ENTER_BUTTON_PASSWORD_RECOVERY_FORM = ".//a[@class='Auth_link__1fOlj' and @href='/login']"   # Кнопка "Войти" в форме восстановления пароля (XPATH)
    PERSONAL_ACCOUNT_BUTTON = ".//p[contains(text(), 'Личный Кабинет')]"   # Кнопка "Личный кабинет" (XPATH)
    EXIT_BUTTON_PERSONAL_ACCOUNT = "Account_button__14Yp3"   # Кнопка "Выход" из личного кабинета (CLASS_NAME)
    RECOVERY_PASSWORD_BUTTON = ".//a[@class='Auth_link__1fOlj' and @href='/forgot-password']"   # Кнопка "Восстановить пароль" (XPATH)
    CONSTRUCTOR_BUTTON = ".//p[contains(., 'Конструктор')]"   # Кнопка "Конструктор" бургеров (XPATH)
    LOGO_BUTTON = ".AppHeader_header__logo__2D0X2"   # Кнопка-логотип "Stellar burgers" на главной странице (CSS)
    BUNS_BUTTON = ".//span[text()='Булки']"   # Кнопка переключения "Булки" в конструкторе (XPATH)
    SAUCES_BUTTON = ".//span[text()='Соусы']"   # Кнопка переключения "Соусы" в конструкторе (XPATH)
    FILLINGS_BUTTON = ".//span[text()='Начинки']"   # Кнопка переключения "Начинки" в конструкторе (XPATH)
    CONSTRUCTOR_SELECTED_SECTION = ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]"   # Локатор выбранного раздела в конструкторе (XPATH)
    CONSTRUCTOR_SELECTED_SECTION_SPAN = ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span"   # Локатор на дочерний SPAN выбранного раздела в конструкторе  (XPATH)
    EMAIL_INPUT = ".//input[@type='text' and @name='name']"   # Поле ввода email (XPATH)
    PASSWORD_INPUT = ".//input[@type='password' and @name='Пароль']"   # Поле ввода пароля (XPATH)
    REGISTER_BUTTON_PERSONAL_ACCOUNT_PAGE = ".//a[contains(@class, 'Auth_link__') and @href='/register']"   # Кнопка "Зарегистрироваться" на странице входа в личный кабинет (XPATH)
    REGISTER_BUTTON_REGISTER_PAGE = ".//button[text()='Зарегистрироваться']"   # Кнопка "Зарегистрироваться" на странице регистрации (XPATH)
    NAME_INPUT_REGISTRATION = ".//label[text()='Имя']/parent::div/input"   # Поле ввода имени при регистрации (XPATH)
    EMAIL_INPUT_REGISTRATION = ".//label[text()='Email']/parent::div/input"   # Поле ввода email при регистрации (XPATH)
    PASSWORD_INPUT_REGISTRATION = ".//label[text()='Пароль']/parent::div/input"   # Поле ввода пароля при регистрации (XPATH)
    ERROR_MESSAGE = ".//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]"   # Сообщение об ошибке (XPATH)
    SAVE_BUTTON_PERSONAL_ACCOUNT = ".//button[text()='Сохранить']"
    FIRST_BUN = ".//img[contains(@class, 'BurgerIngredient_ingredient__image')]"
    LAST_FILLING = ".//img[@alt='Сыр с астероидной плесенью']"

