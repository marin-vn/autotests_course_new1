from atf import *
from atf.ui import *
from pages.Documents import Documents
from pages.timeoff import Dialog
from pages.datetimeoff import Panel
from pages.AuthPages import AuthPages


class Test(TestCaseUI):
    executor = 'Любовь Лисичкина'

    @classmethod
    def setUpClass(cls):
        AuthPages(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.timeoff = Dialog(cls.driver)
        cls.date_time_off = Panel(cls.driver)
        cls.create_doc = Documents(cls.driver)

    def setUp(self):
        """Создание отгула"""

        log('Создать отгул')
        create_doc = Documents(self.driver)
        create_doc.create_document(regulation='Отгул')

        log('Проверить загрузку карточки')
        time_off = Dialog(self.driver)
        time_off.suggest.check_load(1)

    def test_01_no_time(self):
        """Создание отгула без времени"""

        task_data = {'Сотрудник': self.executor, 'Описание': 'Введите возможную причину'}

        log('Заполнить дату')
        self.timeoff.select_date_tomorrow(with_hours=False)

        log('Заполнить данные: Сотрудник и Описание')
        self.timeoff.fill_time_off(catalog=False, **task_data)

        log('На выполнение')
        self.timeoff.run_time_off()
        delay(3)

        log('Закрыть карточку отгула')
        self.timeoff.close()

        log('Проверить данные созданного отгула в реестре')
        self.create_doc.check_timeoff()

        log('Открыть отгул, проверить что введенные данные отображаются')
        self.create_doc.select_item(self.executor)
        self.timeoff.check_executor(task_data.get('Сотрудник'))
        self.timeoff.description.should_be(ContainsText(task_data['Описание']))

        log('Закрыть карточку отгула')
        self.timeoff.close()

        log('Удалить созданный отгул')
        self.create_doc.delete_document(self.executor)

    def test_02_over_time(self):
        """Создание отгула с временем"""

        task_data = {'Сотрудник': self.executor, 'Описание': 'Введите возможную причину'}

        # create_doc = Documents(self.driver)

        log('Выбор сотрудника из справочника')
        self.timeoff.select_executor(self.executor)

        log('Описание')
        self.timeoff.description.type_in('Введите возможную причину')

        log('Заполнить дату, ввести диапазон часов с 12 до 14')
        self.timeoff.select_date_tomorrow(with_hours=True)

        log('На выполнение')
        self.timeoff.run_time_off()
        delay(3)

        log('Закрыть карточку отгула')
        self.timeoff.close()

        log('Проверить данные созданного отгула в реестре')
        self.create_doc.check_timeoff()
        self.create_doc.check_timeoff_hour()

        log('Открыть отгул, проверить что введенные данные отображаются')
        self.create_doc.select_item(self.executor)
        self.timeoff.check_executor(task_data.get('Сотрудник'))
        self.timeoff.description.should_be(ExactText('Введите возможную причину'))
        self.timeoff.hour_off_start.input_readonly.should_be(ContainsText('12:00'))
        self.timeoff.hour_off_end.input_readonly.should_be(ContainsText('14:00'))

        log('Закрыть карточку отгула')
        self.timeoff.close()

        log('Удалить созданный отгул')
        self.create_doc.delete_document(self.executor)
