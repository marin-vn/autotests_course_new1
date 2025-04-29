# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Откройте эталонную задачу по прямой ссылке в новой вкладке браузера
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from atf.ui import *
from atf import log

sbis_ru = 'https://fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
task = 'https://fix-online.sbis.ru/opendoc.html?guid=ef1f1b37-6268-4bd0-abe3-2a5c23fdde43&client=3'
task_title = 'Задача №ZK24041771084 от 17.04.24'


class Auth(Region):
    """Авторизация"""

    login = TextField(By.CSS_SELECTOR, '.controls-InputBase__nativeField', 'Логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled', 'Пароль')


class TaskNewWindow(Region):
    """Эталонная задача в новой вкладке браузера"""

    title = Element(By.CSS_SELECTOR, '[data-qa="Controls-Tabs__item"]', 'Заголовок')
    executor = Element(By.CSS_SELECTOR, '.edws-StaffChooser__itemTpl-name', 'Исполнитель')
    date = Element(By.CSS_SELECTOR, '[data-qa="edo3-Document_docDate"]', 'Дата')
    number = Element(By.CSS_SELECTOR, '[data-qa="edo3-Document_docNumber"]', 'Номер')
    description = Element(By.CSS_SELECTOR, '[name="taskDescrAttr"]', 'Описание')
    author = Element(By.CSS_SELECTOR, '[data-qa="edo3-Sticker__mainInfo"]', 'Автор')


class Test(TestCaseUI):
    """Открытие эталонной задачи по прямой ссылке в новой вкладке браузера"""

    def test(self):
        """Открытие эталонной задачи по прямой ссылке в новой вкладке браузера"""

        self.browser.open(sbis_ru)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact(sbis_title))

        log('Авторизоваться')
        user_login, user_password = 'bigshak', 'bigshak123'
        auth = Auth(self.driver)
        auth.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password.type_in(user_password + Keys.ENTER).should_be(ExactText(user_password))

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('СБИС'))

        log('Открыть эталонную задачу по прямой ссылке в новой вкладке браузера')
        self.browser.create_new_tab(task)
        self.browser.switch_to_opened_window()

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact(task_title))

        log('Проверить соответствие эталону')
        task_new_window = TaskNewWindow(self.driver)
        task_new_window.executor.should_be(ExactText("О'Нил Шакил"))
        task_new_window.date.should_be(ExactText('17 апр, ср'))
        task_new_window.number.should_be(ExactText('...084'))
        task_new_window.description.should_be(ExactText('Да иди ты'))
        task_new_window.author.should_be(ExactText('Карри Стефен'))
