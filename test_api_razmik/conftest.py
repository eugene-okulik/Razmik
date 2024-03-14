import pytest

from endpoints.certain_update import CertainUpdateObject
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.full_update import FullUpdateObject
from endpoints.get_object import GetObject


@pytest.fixture()
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def update_post_endpoint():
    return FullUpdateObject()


@pytest.fixture()
def certain_update_endpoint():
    return CertainUpdateObject()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def get_object():
    return GetObject()


@pytest.fixture()
def post_id(create_post_endpoint):
    payload = {
        "name": "Apple MacBook 17",
        "data": {
            "year": 201779,
            "price": 184977.99,
            "CPU model": "Intel Core i777",
            "Hard disk size": "17 TB"
        }
    }
    create_post_endpoint.create_object(payload)
    yield create_post_endpoint.post_id
