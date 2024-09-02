from controls import *


@templatename("Staff/selectionNew:Stack")
class Stack(CatalogTemplateList):
    """Панель выбора сотрудника-исполнителя"""

    employee_search_field = ControlsSearchInput(SabyBy.DATA_QA, 'addressee-selector-root', 'Поле поиска сотрудника')
    employee_register = ControlsTreeGridView(SabyBy.DATA_QA, 'staffCommon-List_view', 'Реестр сотрудников')

    def executor_choice(self, executor):
        self.search_field.type_in(executor)
        self.executor_tbl.item(contains_text=executor).click()
