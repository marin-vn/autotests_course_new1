from atf import report
from atf.ui import *
from controls import *


class AuthPage(Region):
    """Страница авторизации онлайн"""

    login = ControlsInputText(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__login"]', 'Поле логин')
    password = ControlsInputPassword(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__password"]', 'Поле пароль')

    def auth(self, user_login: str, user_password: str):
        """
        Авторизация
        :param user_login: Логин
        :param user_password: Пароль
        """
        with report.step('Авторизация в онлайн'):
            self.login.type_in(user_login + Keys.ENTER)
            self.login.should_be(ExactText(user_login))
            self.password.type_in(user_password + Keys.ENTER)
            self.password.should_not_be(Displayed, wait_time=True)
            self.check_page_load_wasaby()
