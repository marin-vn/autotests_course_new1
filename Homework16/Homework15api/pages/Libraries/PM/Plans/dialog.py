from atf import *
from atf.ui import *
from controls import *


@templatename("PM/Plans/dialog:Dialog")
class Dialog(DocumentTemplate):
    """Карточка Плана работ"""

    field_plan_object = ControlsLookupInput()
    field_customer = Element(SabyBy.DATA_QA, 'edo3-Sticker__mainInfo', 'Укажите заказчика')
    plan_item_point = Element(By.CSS_SELECTOR, '[title="Пункт плана"]', 'Элемент пункт плана')
    plan_item_tbl = ControlsTreeGridView(By.CSS_SELECTOR, '.plan-PointList__view .controls-Grid',
                                         'Таблица пунктов плана и задач')
    next_phase_btn = ControlsButton(caption='На выполнение')
    field_executor = Element(By.CSS_SELECTOR, '.plan-PointList__employee-name', 'Исполнитель пункта плана')
    close_btn = ControlsButton(By.CSS_SELECTOR, '[title="Закрыть"]', 'Кнопка закрыть')

    def fill_work_plan(self, **plan_data):
        """Заполнение полей документа:
        param plan_data: Объект планирования, Заказчик, Исполнитель, Перечень работ

        """

        if plan_data.get('Объект планирования'):
            self.field_plan_object.should_be(Displayed)
            self.field_plan_object.click().select(plan_data.get('Объект планирования'))
            delay(wait_time=2, message='Открывается панель выбора заказчика')

        if plan_data.get('Заказчик'):
            from Homework15api.pages.Libraries.Addressee.popup import Stack

            self.field_customer.click()
            customer_panel = Stack(self.driver)
            customer_panel.check_open()
            customer_panel.customer_choice(plan_data.get('Заказчик'))

        if plan_data.get('Перечень работ'):
            from Homework15api.pages.Libraries.PM.Plans.point import Dialog as PlanItemDocument

            self.plan_item_point.should_be(Visible, wait_time=True).click()
            plan_item_doc = PlanItemDocument(self.driver)
            plan_item_doc.fill_plan_item(plan_data.get('Исполнитель'), plan_data.get('Перечень работ'))

    def run_document(self):
        """Отправить документ на выполнение"""

        self.next_phase_btn.click()
        self.next_phase_btn.should_not_be(Displayed, wait_time=True)

    def check_document_data(self, **plan_data):
        """ Проверка данных документа:
        param plan_data: Объект планирования, Заказчик, Исполнитель, Перечень работ
        """

        if plan_data.get('Объект планирования'):
            self.field_plan_object.should_be(ExactText(plan_data.get('Объект планирования')))
        if plan_data.get('Заказчик'):
            self.field_customer.should_be(ContainsText(plan_data.get('Заказчик')))
        if plan_data.get('Перечень работ'):
            (self.plan_item_tbl.item(contains_text=plan_data.get('Перечень работ')).
             should_be(ContainsText(plan_data.get('Перечень работ'))))
        if plan_data.get('Исполнитель'):
            (self.plan_item_tbl.item(contains_text=plan_data.get('Исполнитель')).
             should_be(ContainsText(plan_data.get('Исполнитель'))))
        self.close_btn.click()
