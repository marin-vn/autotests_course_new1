# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from atf.ui import *
from atf import log

sbis_ru = 'https://fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'


class Auth(Region):
    """Авторизация"""

    login = TextField(By.CSS_SELECTOR, '.controls-InputBase__nativeField', 'Логин')
    password = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled', 'Пароль')


class Online(Region):
    """Главная страница"""

    tasks = Element(By.CSS_SELECTOR, '[data-qa="Задачи"] [data-qa="NavigationPanels-Accordion__title"]', 'Задачи')
    tasks_for_me = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Задачи на мне')


class Task(Region):
    """Задачи"""

    tabs = CustomList(By.CSS_SELECTOR, '.controls-Tabs__items_wrapper', 'Вкладки')
    in_work = Element(By.CSS_SELECTOR, '[name="tabtasks-in-work"]', 'В работе')
    incoming = Element(By.XPATH, '//div[text()="Входящие"]', 'Входящие')
    marker = Element(By.CSS_SELECTOR, '[data-qa="cell"] [data-qa="marker"]', 'Маркер')
    number_of_tasks = Element(By.CSS_SELECTOR, '[data-qa="controls-EditorList__mainCounter"]', 'Количество задач')
    overdue = Element(By.XPATH, '//div[text()="Просроченные"]', 'Просроченные')
    plus = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]', 'Плюс')
    plus_button_menu = Element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton__dropdownMenu_root_null"]',
                               'Меню кнопки "+"')
    adding_a_folder = Element(By.CSS_SELECTOR, '.icon-CreateFolder', 'Добавление папки')
    new_folder = Element(By.CSS_SELECTOR, '[title="Новая папка"]', 'Новая папка')
    no_tasks = Element(By.CSS_SELECTOR, '[data-qa="hint-EmptyView__title"]', 'В этой папке нет задач')
    popup_menu = Element(By.CSS_SELECTOR, '[templatename="Controls/menu:Popup"]', 'Контекстное меню')
    delete_folder = Button(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Удалить папку')


class NewFolder(Region):
    """Окно добавления папки"""

    folder_add_window = Element(By.CSS_SELECTOR, '[templatename="EDWS3/Utils/userFolder:ConstructionDialog"]',
                                'Окно добавления папки')
    folder_name_input_string = TextField(By.CSS_SELECTOR,
                                         '[templatename="EDWS3/Utils/userFolder:ConstructionDialog"] .controls-Render',
                                         'Строка ввода названия папки')
    folder_name = TextField(By.CSS_SELECTOR, '[template="EDWS3/Utils/userFolder:ConstructionDialog"] .controls-Field',
                            'Название папки')
    save_button = Button(By.CSS_SELECTOR, '.edws-UserFolderDialog__buttonSave', 'Кнопка "Сохранить"')


class DeleteFolder(Region):
    """Окно удаления папки"""

    folder_delete_window = Element(By.CSS_SELECTOR, '[templatename="Controls/popupTemplate:ConfirmationDialog"]',
                                   'Окно удаления папки')
    yes = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Кнопка "Да"')


class Test(TestCaseUI):
    """Создание и удаление папки"""

    def test(self):
        """Создание и удаление папки"""

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

        log('Проверить текст, атрибут и видимость кнопки "Задачи"')
        task = Online(self.driver)
        tasks_txt = 'Задачи'
        task.tasks.should_be(ExactText(tasks_txt), Attribute(innerText=tasks_txt))

        log('Клик на кнопку "Задачи"')
        task.tasks.click()

        log('Переход в реестр "Задачи"')
        task.tasks_for_me.click()

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Задачи на мне'))

        log('Проверить отображение трех вкладок')
        tabs = Task(self.driver)
        tabs.tabs.should_be(CountElements(3))

        log('Проверить текст, атрибут и видимость вкладки "В работе"')
        in_work_txt = 'В работе'
        tabs.in_work.should_be(ExactText(in_work_txt), Attribute(innerText=in_work_txt))

        log('Клик на вкладку "В работе"')
        tabs.in_work.click()

        log('Проверить текст, атрибут и видимость папки "Входящие"')
        incoming_txt = 'Входящие'
        tabs.incoming.should_be(ExactText(incoming_txt), Attribute(innerText=incoming_txt))

        log('Проверить атрибут и видимость маркера')
        tabs.marker.should_be(Attribute(tabintext=None))

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        number_of_tasks_txt = '52'
        tabs.number_of_tasks.should_be(ExactText(number_of_tasks_txt), Attribute(innerText=number_of_tasks_txt))

        log('Клик на папку "Просроченные"')
        tabs.overdue.click()

        log('Проверить текст, атрибут и видимость папки "Просроченные"')
        overdue_txt = 'Просроченные'
        tabs.overdue.should_be(ExactText(overdue_txt), Attribute(innerText=overdue_txt))

        log('Проверить атрибут и видимость маркера')
        tabs.marker.should_be(Attribute(tabintext=None))

        log('Проверить атрибут и видимость кнопки "+"')
        tabs.plus.should_be(Attribute(tabindex='0'))

        log('Клик на кнопку "+"')
        tabs.plus.click()

        log('Проверить атрибут и видимость меню кнопки "+"')
        tabs.plus_button_menu.should_be(Attribute(tabindex='0'))

        log('Проверить атрибут и видимость кнопки добавления папки')
        tabs.adding_a_folder.should_be(Attribute(tabindex=None))

        log('Клик на кнопку добавления папки"')
        tabs.adding_a_folder.click()

        log('Проверить атрибут и видимость окна добавления папки')
        new_folder = NewFolder(self.driver)
        new_folder.folder_add_window.should_be(Attribute(tabindex='0'))

        log('Клик в строку ввода названия папки')
        new_folder.folder_name_input_string.click()

        log('Ввести название папки')
        name = 'Новая папка'
        new_folder.folder_name.type_in(name).should_be(ExactText(name))

        log('Проверить текст, атрибут и видимость кнопки "Сохранить"')
        save_button_txt = 'Сохранить'
        new_folder.save_button.should_be(ExactText(save_button_txt), Attribute(innerText=save_button_txt))

        log('Клик на кнопку "Сохранить"')
        new_folder.save_button.click()

        log('Проверить текст, атрибут и видимость новой папки')
        new_folder_txt = 'Новая папка'
        tabs.new_folder.should_be(ExactText(new_folder_txt), Attribute(innerText=new_folder_txt))

        log('Клик на новую папку')
        tabs.new_folder.click()

        log('Убедиться, что папка пустая')
        no_tasks_txt = 'В этой папке нет задач'
        tabs.no_tasks.should_be(ExactText(no_tasks_txt), Attribute(innerText=no_tasks_txt))

        log('Навести курсор на новую папку и сделать контекстный клик')
        tabs.new_folder.context_click()

        log('Проверить атрибут и видимость контекстного меню')
        tabs.popup_menu.should_be(Attribute(tabindex='0'))

        log('Проверить текст, атрибут и видимость кнопки "Удалить папку"')
        delete_folder_txt = 'Удалить папку'
        tabs.delete_folder.should_be(ExactText(delete_folder_txt), Attribute(innerText=delete_folder_txt))

        log('Клик на кнопку "Удалить папку"')
        tabs.delete_folder.click()

        log('Проверить атрибут и видимость окна удаления папки')
        delete_folder = DeleteFolder(self.driver)
        delete_folder.folder_delete_window.should_be(Attribute(tabindex='0'))

        log('Проверить текст, атрибут и видимость кнопки "Да"')
        yes_txt = 'Да'
        delete_folder.yes.should_be(ExactText(yes_txt), Attribute(innerText=yes_txt))

        log('Клик на кнопку "Да"')
        delete_folder.yes.click()

        log('Проверить текст, атрибут и видимость новой папки')
        new_folder_txt = 'Новая папка'
        tabs.new_folder.should_not_be(ExactText(new_folder_txt), Attribute(innerText=new_folder_txt))
