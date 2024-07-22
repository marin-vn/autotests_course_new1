from atf.ui import *
from controls import *


class AuthPages(Region):
    """Страница авторизации онлайн"""

    login = ControlsInputText()
    password = ControlsInputPassword()
    grecaptcha_badge = Element(By.CSS_SELECTOR, '.grecaptcha-badge', 'Всплывающий баннер')

    def auth(self, login: str, password: str):
        """
        Авторизация на онлайн
        :param login: Логин
        :param password: Пароль
        """

        self.browser.open(self.config.get('SITE'))
        self.grecaptcha_badge.should_be(Displayed)
        self.login.type_in(self.config.get('USER_LOGIN'))
        self.login.should_be(ExactText(login))
        self.login.send_keys(Keys.ENTER)
        self.password.type_in(self.config.get('USER_PASSWORD'))
        self.password.send_keys(Keys.ENTER)
        self.password.should_not_be(Displayed, wait_time=True)
        self.check_page_load_wasaby()
