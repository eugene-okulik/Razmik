import allure
import requests

from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    post_id = None

    def __init__(self):
        self.json = None
        self.response = None

    @allure.title("Создания обьектов с разными данными")
    @allure.description("Создаем 3 разных обьекта с разными данными в body")
    @allure.feature("Posts")
    @allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
    @allure.severity('Высокий')
    @allure.step("Create new object")
    def create_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response
