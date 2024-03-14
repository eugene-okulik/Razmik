import allure
import requests

from endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    def __init__(self):
        self.json = None
        self.response = None

    @allure.step("Get object")
    @allure.title("Получени инфы обьекта")
    @allure.description("Получение информации о существующем обьекте")
    @allure.feature("Get")
    @allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
    @allure.severity('Высокий')
    @allure.story("Get object")
    def get_object(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{post_id}', headers=headers)
        self.json = self.response.json()
        return self.response
