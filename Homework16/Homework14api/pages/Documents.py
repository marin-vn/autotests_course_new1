from atf.ui import *
from controls import *
from datetime import datetime, timedelta


class Documents(Region):
    """Документы"""
    create_doc = ExtControlsDropdownAddButton()
    timeoff_list = ControlsTreeGridView(SabyBy.DATA_QA, 'wtd-List', 'Реестр')
    timeoff_description = Element(By.CSS_SELECTOR, '.wtd-List__mainInfo-noteText', 'Описание')
    timeoff_date = Element(SabyBy.DATA_QA, 'DTStartFormat', 'Дата')
    timeoff_hours = Element(SabyBy.DATA_QA, 'DurationPeriod', 'Время')

    def open(self):
        """Переходим в 'Сотрудники' -> 'Графики работ', вкладка 'Документы'"""

        self.browser.open(f'{self.browser.site}/page/work-schedule-documents')
        self.check_page_load_wasaby()

    def create_document(self, regulation='Отгул'):
        """
        Создание отгула
        :param regulation:
        """

        self.create_doc.select(regulation)

    def check_timeoff(self, employee='Любовь Лисичкина', cause='Введите возможную причину'):
        """
        Создание карточки отгула
        :param employee: Сотрудник
        :param cause: Причина
        """

        date = (datetime.today() + timedelta(days=1)).strftime("%d.%m.%y")
        create_doc = Documents(self.driver)
        timeoff = create_doc.timeoff_list.item(contains_text=employee)
        create_doc.timeoff_description.add_parent(timeoff)
        create_doc.timeoff_description.should_be(ExactText(cause))
        create_doc.timeoff_date.add_parent(timeoff)
        create_doc.timeoff_date.should_be(ExactText(date))

    def check_timeoff_hour(self):
        """Проверить отображение указанного времени в документе"""

        self.timeoff_hours.should_be(ContainsText('12:00-14:00'))

    def open_item(self, search_str: str):
        """
        Открыть запись
        :param search_str:
        """
        self.timeoff_list.item(contains_text=search_str).click()
