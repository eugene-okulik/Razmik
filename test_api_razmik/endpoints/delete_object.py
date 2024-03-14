import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    def __init__(self):
        self.json = None
        self.response = None

    @allure.step("Delete object")
    @allure.title("Удаление обьекта")
    @allure.description("Удаление существующего обьекта")
    @allure.feature("Delete")
    @allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
    @allure.severity('Высокий')
    @allure.story("Delete whole object")
    def delete_object(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{post_id}', headers=headers)
        self.json = self.response.json()
        return self.response
