import requests
import pytest
import allure


@allure.title("Создания обьектов с разными данными")
@allure.description("Создаем 3 разных обьекта с разными данными в body")
@allure.feature("Posts")
@allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
@allure.severity('Высокий')
@allure.story("Create objects")
@pytest.mark.critical
@pytest.mark.parametrize("body", [
    {
        "name": "Apple MacBook 17",
        "data": {
            "year": 201779,
            "price": 184977.99,
            "CPU model": "Intel Core i777",
            "Hard disk size": "17 TB"
        }
    },
    {
        "name": "Some Other Laptop",
        "data": {
            "year": 2020,
            "price": 1299.99,
            "CPU model": "AMD Ryzen",
            "Hard disk size": "512 GB"
        }
    },
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
])
def test_create_object(body, some_func, for_testing):
    with allure.step('Подготовка данных для запроса'):
        headers = {"content-type": "application/json"}
    with allure.step('Отправка запроса с 3 разными body'):
        res = requests.post("https://api.restful-api.dev/objects", json=body, headers=headers)
    with allure.step('Сервер вернул код ответа 200'):
        assert res.status_code == 200, "Status code error"


@allure.title("Полное обновление обьекта")
@allure.description("Обновляем все данные в существующем обьекте")
@allure.feature("Put")
@allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
@allure.severity('Средний')
@allure.story("Full update object")
@pytest.mark.medium
def test_full_update_object(create_object):
    with allure.step('Подготовка данных для запроса'):
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
        headers = {"content-type": "application/json"}
    with allure.step('Отправка запроса на обновление данных обьекта'):
        res = requests.put(f"https://api.restful-api.dev/objects/{create_object}", json=body, headers=headers)
    with allure.step('Цена в теле запроса соответсвует новой цене на которую обновляли'):
        assert res.json()['data']['price'] == 2049.99


@allure.title("Частичное обновление обьекта")
@allure.description("Обновляем выборочно данные в существующем обьекте")
@allure.feature("Patch")
@allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
@allure.severity('Средний')
@allure.story("Certain update object")
def test_certain_update_object(create_object):
    with allure.step('Подготовка данных для запроса'):
        body = {
            "name": "Apple MacBook Pro 16 (Updated Name)"
        }
        headers = {"content-type": "application/json"}
    with allure.step('Отправка запроса на обновление данных обьекта'):
        res = requests.patch(f"https://api.restful-api.dev/objects/{create_object}", json=body, headers=headers)
    with allure.step('Поле "name" == обновленному полю из этого запроса'):
        assert res.json()['name'] == "Apple MacBook Pro 16 (Updated Name)"


@allure.title("Удаление обьекта")
@allure.description("Удаление существующего обьекта")
@allure.feature("Delete")
@allure.issue("https://okulik.by/kabinet/group?groupId=44", 'Example of link')
@allure.severity('Высокий')
@allure.story("Delete whole object")
def test_delete_object(create_object):
    with allure.step('Отправка запроса на удаление данных обьекта'):
        res_delete = requests.delete(f"https://api.restful-api.dev/objects/{create_object}")
    with allure.step('Отправка запроса на получение данных обьекта об удаленном обьекте'):
        res_get = requests.get(f"https://api.restful-api.dev/objects/{create_object}")
    with allure.step('Код ответа с удаление обьекта == 200'):
        assert res_delete.status_code == 200
    with allure.step('Код ответа с получения информации об удаленном обьекте == 404'):
        assert res_get.status_code == 404
