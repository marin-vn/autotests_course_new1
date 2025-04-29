from controls import *
from atf.ui import *
from datetime import datetime, timedelta
from pages.datetimeoff import Panel


@templatename("WorkTimeDocuments/timeoff:Dialog")
class Dialog(DocumentTemplate):
    """Карточка отгула"""

    calendar = ControlsDatePicker(By.CSS_SELECTOR, '.wtd-dayTimeSelector-inputInlineHeight', 'Дата')
    hour_off_start = ControlsInputMask(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__start', 'Часы начало')
    hour_off_end = ControlsInputMask(SabyBy.DATA_QA, 'wtd-TimeIntervalMinutes__end', 'Часы конец')
    hours_off = Button(By.CSS_SELECTOR, '.icon-TimeSkinny', 'Часы отгула')
    suggest = Element(SabyBy.DATA_QA, 'controls-suggestPopup', 'Саджест по сотрудникам')
    executor = ControlsLookupInput(SabyBy.DATA_QA, 'staff-Lookup__input', 'Исполнитель')
    description = RichEditorExtendedEditor(SabyBy.DATA_QA, 'wtd-Base__comment', 'Причина отгула')
    for_execution = ControlsButton(By.CSS_SELECTOR, '.edo3-PassageButton', 'На выполнение')
    agree_on_time_off = ControlsButton(SabyBy.DATA_QA, 'extControls-doubleButton__caption', 'Согласовать отгул')
    change = ControlsButton(SabyBy.DATA_QA, 'extControls-singleButton__caption', 'Изменить')

    def select_date_tomorrow(self, with_hours, start_hour='1200', end_hour='1400'):
        """Заполнение даты отгула завтрашним днем"""

        self.calendar.click()
        self.calendar.calendar_panel.set_period((datetime.today() + timedelta(days=1)).strftime("%d.%m.%y"))
        if with_hours:
            self.hours_off.click()
            self.hour_off_start.type_in(start_hour)
            self.hour_off_end.type_in(end_hour)

    def fill_time_off(self, catalog, **kwargs):
        """Заполнить отгул"""

        self.check_open()
        if 'Сотрудник' in kwargs.keys():
            if catalog:
                self.executor.select_from_catalog(kwargs['Сотрудник'])
            else:
                self.executor.autocomplete_search(kwargs['Сотрудник'])
            self.executor.should_be(ContainsText(kwargs['Сотрудник']))
        if 'Описание' in kwargs.keys():
            self.description.type_in(kwargs['Описание'])
            self.description.should_be(ContainsText(kwargs['Описание']))

    def run_time_off(self):
        """Отправить на выполнение"""

        self.for_execution.click()
        panel = Panel(self.driver)
        panel.to_myself.click()
        panel.agree.click()

    def open_to_redaction(self):
        """Открыть на редактирования"""

        if self.change.is_displayed:
            self.change.click()
        self.change.should_not_be(Displayed)

    def select_executor(self, executor_name):
        """
        :param executor_name: исполнитель
        """
        self.executor.click().select(executor_name)

    def check_executor(self, executor_name):
        """
        :param executor_name: исполнитель
        """
        self.executor.should_be(ContainsText(executor_name))
