from controls import *
from atf.ui import *


@templatename('Addressee/popup:Stack')
class Stack(CatalogTemplateList):
    """Справочник выбора сотрудника-заказчика"""

    employee_search_field = ControlsSearchInput(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"]',
                                                'Поиск заказчика')
    employee_register = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="staffCommon-List_view"] .controls-Grid',
                                             'Таблица заказчиков')

    def search_employee(self, executor):
        self.employee_search_field.type_in(executor)
        self.employee_register.item(contains_text=executor).click()
