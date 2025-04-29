from atf import report
from atf.ui import Displayed
from controls import *


@templatename("PM/Plans/point:Dialog")
class Dialog(DocumentTemplate):
    """Карточка Пункта плана"""

    executor_btn = ControlsButton(By.CSS_SELECTOR, '[title="Добавить исполнителя"]', 'Кнопка добавить исполнителя')
    field_list_of_works = ControlsInputArea()
    save_btn = ControlsButton(By.CSS_SELECTOR, '[data-qa="edo3-ReadOnlyStateTemplate__saveButton"]', 'Кнопка сохранить')

    def fill_plan_item(self, executor, list_work):
        """ Заполнение карточки пункта плана
        :param executor: Исполнитель
        :param list_work: Перечень работ
        """

        with report.step('Заполняем карточку пункта плана'):
            from Homework15api.pages.Libraries.Staff.selectionNew import Stack

            self.executor_btn.click()
            executor_panel = Stack(self.driver)
            executor_panel.check_open()
            executor_panel.executor_choice(executor)
            self.field_list_of_works.type_in(list_work)
            self.save_btn.click()
            self.save_btn.should_not_be(Displayed)
