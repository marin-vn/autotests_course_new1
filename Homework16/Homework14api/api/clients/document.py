from atf.api.base_api_ui import BaseApiUI


class Document(BaseApiUI):
    """
    API методы объекта Document
    """

    def delete_document(self, ido):
        """
        Метод для удаления документов
        param ido: Идентификатор документа
        """

        params = {'ИдО': ido}

        self.client.call_rvalue(method="Документ.УдалитьДокументы", **params)
