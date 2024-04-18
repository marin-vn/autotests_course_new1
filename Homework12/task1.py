# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf.ui import *
from atf import *

sbis_ru = 'https://fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'


class Auth(Region):
    """Авторизация"""

    login = TextField(By.CSS_SELECTOR, '.controls-InputBase__nativeField', 'Логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled', 'Пароль')


class Online(Region):
    """Главная страница"""

    contacts = Element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]', 'Контакты')
    sub_contacts = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Сабкнопка')


class Contacts(Region):
    """Контакты"""

    tab = CustomList(By.CSS_SELECTOR, '.controls-Tabs__item', 'Вкладки')
    tab_contacts = Element(By.CSS_SELECTOR, '[title="Диалоги"]', 'Диалоги')
    plus = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]', 'Плюс')
    messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item', 'Список сообщений')


class Message(Region):
    """Сообщение"""

    search_line = TextField(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] [data-qa="controls-Render__field"]',
                            'Строка поиска')
    fio = TextField(By.CSS_SELECTOR, '.controls-InputBase__nativeField', 'ФИО')
    employee = Element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]', 'Сотрудник')
    entry_field = TextField(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]', 'Поле ввода')
    msg = Element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]', 'Сообщение')
    send_button = Button(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]', 'Отправить')
    close = Button(By.CSS_SELECTOR, '[data-qa="controls-stack-Button__close"]', 'Закрыть')
    delete = Button(By.CSS_SELECTOR, '[data-qa = "remove"]', 'Удалить')


class Test(TestCaseUI):
    """Создание, отправка и удаление сообщения"""

    def test01_message_create_send_delete(self):
        """Создание, отправка и удаление сообщения"""

        log('Открыть сайт')
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

        log('Проверить текст, атрибут и видимость кнопки "Контакты"')
        contact = Online(self.driver)
        contacts_txt = 'Контакты'
        contact.contacts.should_be(ExactText(contacts_txt), Attribute(innerText=contacts_txt))

        log('Клик на кнопку "Контакты"')
        contact.contacts.click()

        log('Переход в реестр "Контакты"')
        contact.sub_contacts.click()

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Контакты'))

        log('Проверить отображение трех вкладок')
        tabs = Contacts(self.driver)
        tabs.tab.should_be(CountElements(3))

        log('Проверить текст, атрибут и видимость вкладки "Диалоги"')
        tab_contacts_txt = 'Диалоги'
        tabs.tab_contacts.should_be(ExactText(tab_contacts_txt), Attribute(innerText=tab_contacts_txt))

        log('Клик на вкладку "Диалоги"')
        tabs.tab_contacts.click()

        log('Проверить атрибут и видимость кнопки "+"')
        tabs.plus.should_be(Attribute(tabindex='0'))

        log('Клик на кнопку "+"')
        delay(1)
        tabs.plus.click()

        log('Клик в строку поиска')
        message = Message(self.driver)
        message.search_line.click()

        log('Ввести ФИО')
        name = "О'Нил Шакил"
        message.fio.type_in(name + Keys.ENTER).should_be(ExactText(name))

        log('Проверить текст, атрибут и видимость сотрудника')
        employee_txt = "О'Нил Шакил"
        message.employee.should_be(ExactText(employee_txt), Attribute(tabindex='0'))

        log('Клик на сотрудника')
        message.employee.click()

        log('Проверить атрибут и видимость поля ввода')
        message.entry_field.should_be(Attribute(role='textbox'))

        log('Ввести текст сообщения')
        message_text = 'Hi'
        message.msg.type_in(message_text).should_be(ExactText(message_text))

        log('Проверить атрибут и видимость кнопки "Отправить"')
        message.send_button.should_be(Attribute(tabindex='-1'))

        log('Клик на кнопку "Отправить"')
        delay(1)
        message.send_button.click()

        log('Закрыть сообщение')
        message.close.click()

        log('Навести курсор на сообщение и открыть')
        tabs.messages.item(1).click()

        log('Клик на кнопку "Удалить"')
        message.delete.click()

        log('Проверить отображение удаленного сообщения')
        tabs.messages.should_not_be(Displayed)
