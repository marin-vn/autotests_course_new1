from atf.api.base_api_ui import BaseApiUI
from Homework16api.clients.staff import Staff
from atf import *


class StaffFunctions(BaseApiUI):
    """Методы объекта Staff"""

    def check_staff_by_fio(self, fio):
        """
        Получаем данные сотрудника и сравниваем их с эталонными
        param fio: ФИО сотрудника
        """

        assert_that(fio, not_equal(""), "Нельзя передавать пустую строку")
        staff_list = Staff(self.client).list(search=fio.get('ФИО'))
        for staff in staff_list.result:
            if staff.get("Employee"):
                assert_that(staff.get("BirthDate"), equal_to(fio['Дата рождения']), "Дата рождения")
                assert_that(staff.get("HiredDate"), equal_to(fio['Дата приема на работу']),
                            "Дата приема на работу")
                assert_that(staff.get("Position"), equal_to(fio['Должность']),
                            "Должность")
                assert_that(staff.get("User"), equal_to(fio['ID в облаке']),
                            "ID в облаке")
                assert_that(staff.get("Email"), equal_to(fio['Электронный адрес']),
                            "Электронный адрес")
                assert_that(staff.get("MobilePhone"), equal_to(fio['Мобильный телефон']),
                            "Мобильный телефон")
