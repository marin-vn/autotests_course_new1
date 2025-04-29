from atf import *
from atf.api.json_rpc import JsonRpcClient
from Homework16api.wrappers.staff_functions import StaffFunctions


class TestStaff(TestCase):
    """
    Проверка сотрудника
    """

    client = None
    staff_info = "Да иди ты"

    @classmethod
    def setUpClass(cls):
        cls.client = JsonRpcClient(cls.config.get('SITE'), verbose_log=2)
        cls.client.auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

        cls.staff_functions = StaffFunctions(cls.client)

    def test_check_staff_data(self):
        """
        Сравнение данных о сотруднике с эталонными
        """

        staff_info = {'ФИО': 'Карри Стефен',
                      'Дата рождения': None, 'Дата приема на работу': '2025-04-25',
                      'Должность': 'Бобик', 'Электронный адрес': 'curry@mail.ru',
                      'Мобильный телефон': '+7 (913) 604-72-00', 'ID в облаке': 200068244}

        with report.step('Проверка данных сотрудника'):

            self.staff_functions.check_staff_by_fio(staff_info)
