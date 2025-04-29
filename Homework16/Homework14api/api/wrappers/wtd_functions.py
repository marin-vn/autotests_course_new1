from atf.api.base_api_ui import BaseApiUI
from Homework14api.api.clients.time_off import WTD
from Homework14api.api.clients.document import Document
from atf import *


class WTDFunctions(BaseApiUI):
    """Методы объекта WTD"""

    def delete_timeoff_by_staff(self, staff):
        """
        Удалить отгул
        param staff: ФИО сотрудника, по которому ищем
        """

        assert_that(staff, not_equal(""), "Нельзя передавать пустую строку")

        time_off_list = WTD(self.client).list(search=staff, type_doc='Отгул', date_end=None, date_start=None,
                                              my_doc='От меня')
        document = Document(self.client)
        for time_off in time_off_list.result:
            if staff in time_off['EmployeeFIOList']:
                document.delete_document(ido=time_off['РП.Документ']['ИдО'])
