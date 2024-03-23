# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'

try:
    driver.get(sbis_site)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Авторизоваться')
    sleep(1)
    user_login, user_password = 'bigshak', 'bigshak123'
    login = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    password.send_keys(user_password, Keys.ENTER)

    print('Проверить адрес сайта и заголовок страницы')
    sleep(2)
    assert 'fix-online.sbis.ru' in driver.current_url
    assert driver.title == 'СБИС'

    print('Проверить отображение аккордеона')
    sleep(1)
    accordion = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__container')
    assert accordion.is_displayed(), 'Аккордеон не отображается'

    print('Проверить текст, атрибут и видимость кнопки "Контакты"')
    contacts_txt = 'Контакты'
    contacts = driver.find_element(By.CSS_SELECTOR,
                                   '[data-qa="Контакты"] [data-qa="NavigationPanels-Accordion__title"]')
    assert contacts.text == contacts_txt
    assert contacts.get_attribute("innerText") == contacts_txt

    print('Клик на кнопку "Контакты"')
    sleep(1)
    contact = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    action_chains = ActionChains(driver)
    action_chains.click(contact).perform()

    print('Перейти в реестр "Контакты"')
    sleep(2)
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    contacts.click()

    print('Проверить адрес сайта и заголовок страницы')
    sleep(2)
    assert 'fix-online.sbis.ru' in driver.current_url
    assert driver.title == 'Контакты'

    print('Проверить отображение трех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.controls-Tabs__item')
    assert len(tabs) == 3

    print('Проверить текст, атрибут и видимость вкладки "Диалоги"')
    sleep(2)
    tab_contacts_txt = 'Диалоги'
    tab_contacts = driver.find_element(By.CSS_SELECTOR, '[title="Диалоги"]')
    assert tab_contacts.text == tab_contacts_txt
    assert tab_contacts.get_attribute("innerText") == tab_contacts_txt
    assert tab_contacts.is_displayed(), 'Элемент не отображается'

    print('Клик на вкладку "Диалоги"')
    tab_contacts.click()

    print('Проверить атрибут и видимость кнопки "+"')
    sleep(1)
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert contacts.get_attribute("tabindex") == "0"
    assert contacts.is_displayed(), 'Элемент не отображается'

    print('Клик на кнопку "+"')
    sleep(1)
    contacts.click()

    print('Проверить видимость строки поиска')
    sleep(3)
    search_line = driver.find_element(By.CSS_SELECTOR,
                                      '[data-qa="addressee-selector-root"] [data-qa="controls-Render__field"]')
    assert search_line.is_displayed(), 'Элемент не отображается'

    print('Клик в строку поиска')
    search_line.click()

    print('Ввести ФИО')
    sleep(2)
    name = "О'Нил Шакил"
    fio = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__headerContentTemplate .controls-Field')
    fio.send_keys(name)
    assert fio.get_attribute('value') == name

    print('Проверить текст, атрибут и видимость сотрудника')
    sleep(1)
    employee_txt = "О'Нил Шакил"
    employee = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert employee.text == employee_txt
    assert employee.get_attribute("tabindex") == "0"
    assert employee.is_displayed(), 'Элемент не отображается'

    print('Клик на сотрудника')
    employee.click()

    print('Проверить атрибут и видимость поля ввода')
    sleep(2)
    entry_field = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert entry_field.get_attribute("role") == "textbox"
    assert entry_field.is_displayed(), 'Элемент не отображается'

    print('Ввести текст сообщения')
    sleep(1)
    message = 'Привет'
    msg = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    msg.send_keys(message)
    assert msg.get_attribute('innerText') == message

    print('Проверить атрибут и видимость кнопки "Отправить"')
    sleep(1)
    send_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    assert send_button.get_attribute("tabindex") == "-1"
    assert send_button.is_displayed(), 'Элемент не отображается'

    print('Клик на кнопку "Отправить"')
    send_button.click()

    print('Проверить атрибут и видимость кнопки "Закрыть"')
    sleep(1)
    close_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-stack-Button__close"]')
    assert close_button.get_attribute("tabindex") == "-1"
    assert close_button.is_displayed(), 'Элемент не отображается'

    print('Клик на кнопку "Закрыть')
    close_button.click()

    print('Проверить текст, атрибут и видимость созданного сообщения')
    sleep(2)
    mesg_txt = "Привет"
    mesg = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert mesg.text == mesg_txt
    assert mesg.get_attribute("tabindex") == "0"
    assert mesg.is_displayed(), 'Элемент не отображается'

    print('Навести курсор на сообщение и открыть')
    sleep(3)
    ms = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item')
    action_chains = ActionChains(driver)
    action_chains.click(ms).perform()

    print('Проверить видимость кнопки "Удалить"')
    sleep(3)
    delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="remove"]')
    assert delete.is_displayed(), 'Элемент не отображается'

    print('Клик на кнопку "Удалить"')
    delete.click()

    print('Проверить отображение удаленного сообщения')
    sleep(3)
    mss = driver.find_element(By.CSS_SELECTOR, '.hint-Template-Wrapper_emptyTemplate')
    assert mss.is_displayed(), 'Удаленное сообщение отображается'
finally:
    driver.quit()
