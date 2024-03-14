import allure
import requests

from endpoints.endpoint import Endpoint


class CertainUpdateObject(Endpoint):

    def __init__(self):
        self.json = None
        self.response = None

    @allure.step("Certain update object")
    @allure.title("Частичное обновление обьекта")
    @allure.description("Обновляем выборочно данные в существующем обьекте")
    @allure.feature("Patch")
    @allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
    @allure.severity('Средний')
    @allure.story("Certain update object")
    def certain_update_object(self, payload, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{post_id}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response
