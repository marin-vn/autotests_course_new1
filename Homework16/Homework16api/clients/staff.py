from atf.api.base_api_ui import BaseApiUI
from atf.api.helpers import *


class Staff(BaseApiUI):
    """
    API методы объекта Staff
    """

    def list(self, search):
        """
        Метод для получения списка сотрудников
        param search: Текст поискового запроса
        """

        params = generate_record_list(SearchString=search)

        return self.client.call_rrecordset(method="Staff.WasabyList", **params).result
