from atf.api.base_api_ui import BaseApiUI
from Homework15api.api.clients.work_plan import WorkPlan
from Homework15api.api.clients.document import Document
from atf import *


class WorkPlanFunctions(BaseApiUI):
    """Методы объекта WorkPlan"""

    def delete_plan_work_by_mask(self, mask):
        """
        Удалить план работ
        param mask: Название, по которому ищем
        """

        assert_that(mask, not_equal(""), "Нельзя передавать пустую строку")

        work_plan_list = WorkPlan(self.client).list_of_plans(filter_by_mask=mask)
        document = Document(self.client)
        for work_plan in work_plan_list.result:
            if mask in work_plan['Название']:
                document.delete_document(ido=work_plan['@Документ'])
