from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WTD(BaseApiUI):
    """
    API методы объекта WTD
    """

    def list(self, search, type_doc, date_end, date_start, my_doc):
        """
        Метод для получения списка отгулов
        param type_doc: Название типа документа
        param date_end: Дата начала периода
        param date_start: Дата конца периода
        param my_doc:Фильтр по автору
        param search: Текст поискового запроса
        """

        params = generate_record_list(ТипДокумента=type_doc, ФильтрДатаП=(date_end, 'Дата'),
                                      ФильтрДатаС=(date_start, 'Дата'), ФильтрМоиДокументы=my_doc, ФильтрПоиска=search)

        return self.client.call_rrecordset(method="WTD.List", **params).result
