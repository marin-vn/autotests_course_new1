from controls import *


@templatename("Staff/selectionNew:Stack")
class Stack(CatalogTemplateList):
    """Панель выбора сотрудника-исполнителя"""

    search_field = ControlsSearchInput(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"]', 'Поиск исполнителя')
    executor_tbl = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="staffCommon-List_view"] .controls-Grid',
                                        'Таблица исполнителей')

    def executor_choice(self, executor):
        self.search_field.type_in(executor)
        self.executor_tbl.item(contains_text=executor).click()
