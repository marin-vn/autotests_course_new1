from atf import report
from atf.ui import TestCaseUI
from pages.AuthPage import AuthPage
from pages.WorkPlans import WorkPlans
from atf.api.json_rpc import JsonRpcClient
from Homework15api.api.wrappers.work_plan_functions import WorkPlanFunctions


class TestWorkOffDoc(TestCaseUI):
    work_plan_functions = None
    mask = 'Объект'

    @classmethod
    def setUpClass(cls):
        with report.step('Авторизация'):
            cls.browser.open(cls.config.get('SITE'))
            AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

        with report.step('Удаление старых данных АТ'):
            cls.client = JsonRpcClient(cls.config.get('SITE'), verbose_log=2)
            cls.client.auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

            cls.work_plan_functions = WorkPlanFunctions(cls.client)
            cls.work_plan_functions.delete_plan_work_by_mask(cls.mask)

    def setUp(self):
        with report.step('Переходим в реестр Графики работ'):
            WorkPlans(self.driver).open_registry()

    def test_01(self):
        """Создать план работ и убедиться, что он появился в реестре и при его открытии, значения в полях сохранились"""

        plan_data = {'Объект планирования': 'ОБЪЕКТ АВТОТЕСТ', 'Заказчик': 'Лев Официантович',
                     'Исполнитель': 'Кейт Кинкэйд', 'Перечень работ': 'Написать автотест'}
        data_for_check = ['ОБЪЕКТ АВТОТЕСТ)', 'Лев Официантович', 'Написать автотест']

        work_plan_page = WorkPlans(self.driver)
        with report.step('Создаем документ План работ'):
            doc_card = work_plan_page.create_document()
            doc_card.fill_work_plan(**plan_data)
            doc_card.run_document()
        with report.step('Проверяем наличие документа в реестре'):
            work_plan_page.check_document('Проверить годовой отчет', 'Качусов Ф', 'Финансы (ЗУП КОРП 3.1 КЭДО НАЛИ)')
            work_plan_page.open_document(data_for_check[2])
        with report.step('Проверяем данные документа'):
            doc_card.check_document_data(**plan_data)

    @classmethod
    def tearDownClass(cls):
        with report.step('Удаление данных АТ'):
            cls.work_plan_functions.delete_plan_work_by_mask(cls.mask)
