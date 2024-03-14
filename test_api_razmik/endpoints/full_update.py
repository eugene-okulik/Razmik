import allure
import requests

from endpoints.endpoint import Endpoint


class FullUpdateObject(Endpoint):

    def __init__(self):
        self.json = None
        self.response = None

    @allure.step("Full update object")
    @allure.title("Полное обновление обьекта")
    @allure.description("Обновляем все данные в существующем обьекте")
    @allure.feature("Put")
    @allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
    @allure.severity('Средний')
    @allure.story("Full update object")
    def full_update_object(self, payload, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{post_id}', json=payload, headers=headers)
        self.json = self.response.json()
        return self.response
