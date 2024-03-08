import requests
import pytest


@pytest.fixture()
def create_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    res = requests.post("https://api.restful-api.dev/objects", json=body, headers=headers)
    post_id = res.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


@pytest.fixture()
def for_testing():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session')
def some_func():
    print('Start testing')
    yield
    print('Testing completed')


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
    headers = {"content-type": "application/json"}
    res = requests.post("https://api.restful-api.dev/objects", json=body, headers=headers)
    assert res.status_code == 200, "Status code error"


@pytest.mark.medium
def test_full_update_object(create_object):
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
    res = requests.put(f"https://api.restful-api.dev/objects/{create_object}", json=body, headers=headers)
    assert res.json()['data']['price'] == 2049.99


def test_certain_update_object(create_object):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {"content-type": "application/json"}
    res = requests.patch(f"https://api.restful-api.dev/objects/{create_object}", json=body, headers=headers)
    assert res.json()['name'] == "Apple MacBook Pro 16 (Updated Name)"
