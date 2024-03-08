import pytest
import requests


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