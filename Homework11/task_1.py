# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    driver.get(sbis_site)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    print('Проверить текст, атрибут и видимость кнопки "Контакты"')
    button_txt = 'Контакты'
    start_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    assert start_btn.text == button_txt
    assert start_btn.get_attribute('innerText') == button_txt

    print('Перейти в раздел "Контакты"')
    assert start_btn.is_displayed(), 'Элемент не отображается'
    start_btn.click()

    print('Проверить адрес сайта и заголовок страницы')
    assert 'https://sbis.ru/contacts' in driver.current_url
    assert driver.title == 'СБИС Контакты — Омская область'

    print('Навести курсор на баннер Тензор, кликнуть по нему')
    sleep(1)
    banner = driver.find_element(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    banner.click()

    print('Перейти на страницу https://tensor.ru/')
    driver.switch_to.window(driver.window_handles[1])

    print('Проверить адрес сайта и заголовок страницы')
    assert 'tensor.ru' in driver.current_url
    assert driver.title == 'Тензор — IT-компания'

    print('Проверить отображение блока новости "Сила в людях"')
    sleep(1)
    block = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    driver.execute_script("arguments[0].scrollIntoView();", block)
    assert block.is_displayed(), 'Блок новости "Сила в людях" не отображается'

    print('Навести курсор на кнопку "Подробнее", кликнуть по ней')
    sleep(1)
    button = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-link[href="/about"]')
    button.click()

    print('Проверить адрес сайта и заголовок страницы')
    sleep(1)
    assert 'tensor.ru/about' in driver.current_url
    assert driver.title == 'О компании | Тензор — IT-компания'
finally:
    driver.quit()
