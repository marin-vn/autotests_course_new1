from controls import *
from Homework15.pages.Libraries.Staff.selectionNew import Stack


@templatename("PM/Plans/point:Dialog")
class Dialog(DocumentTemplate):
    """Карточка Пункта плана"""

    list_of_works = ControlsInputArea()
    executor = ControlsButton(By.CSS_SELECTOR, '[title="Добавить исполнителя"]', 'Кнопка добавить исполнителя')
    save = ControlsButton(SabyBy.DATA_QA, 'edo3-ReadOnlyStateTemplate__saveButton', 'Кнопка сохранить')

    def fill_plan_item(self, list_work, executor):
        """ Заполнение карточки пункта плана
        :param executor: Исполнитель
        :param list_work: Перечень работ
        """

        stack = Stack(self.driver)
        self.list_of_works.type_in(list_work)
        self.executor.click()
        stack.executor_choice(executor)
        self.save.click()
