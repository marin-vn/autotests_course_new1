from atf.ui import *
from controls import *
from lection_15.pages.Libraries.PM.Plans.dialog import Dialog


class WorkPlans(Region):
    """Реестр Планы работ"""

    add_button = ExtControlsDropdownAddButton()
    plan_objects_table = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail_master .controls-Grid',
                                              'Таблица наименований объектов')
    documents_table = ControlsTreeGridView(By.CSS_SELECTOR, '.edo3-Browser-scroll-container .controls-Grid',
                                           'Таблица с документами')

    def open_registry(self):
        """Переход в реестр Планы работ"""

        self.browser.open(f'{self.browser.site}/page/plans')
        self.check_page_load_wasaby()
        self.plan_objects_table.check_load()
        self.documents_table.check_load()

    def create_document(self):
        """Создание документа План работ"""

        self.add_button.select('План работ')
        doc_card = Dialog(self.driver)
        doc_card.check_open()
        return doc_card

    def check_document(self, *data_for_check):
        """Проверка наличия документа в реестре:
        type data_for_check: Перечень работ, Исполнитель
        """

        self.documents_table.check_load()
        for data in data_for_check:
            self.documents_table.item(contains_text=data).should_be(Displayed)

    def open_document(self, doc_name):
        """ Открытие карточки документа
        :param doc_name: str Название документа
        """

        self.documents_table.item(contains_text=doc_name).click()
