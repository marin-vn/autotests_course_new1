from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class WorkPlan(BaseApiUI):
    """
    API методы объекта WorkPlan
    """

    def list_of_plans(self, filter_by_mask):
        """
        Метод для получения списка планов работ
        param filter_by_mask: Поиск по маске
        """

        params = generate_record_list(ФильтрПоМаске=filter_by_mask)

        return self.client.call_rrecordset(method="ПланРабот.СписокПланов", **params).result
