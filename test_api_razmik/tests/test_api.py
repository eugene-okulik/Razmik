import pytest


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
def test_create_object(create_post_endpoint, body):
    create_post_endpoint.create_object(payload=body)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_that_status_is_200()


@pytest.mark.medium
def test_full_update_object(update_post_endpoint, create_post_endpoint, post_id):
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
    update_post_endpoint.full_update_object(body, post_id)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_price_in_body(body['data']['price'])


def test_certain_update_object(certain_update_endpoint, post_id):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    certain_update_endpoint.certain_update_object(body, post_id)
    certain_update_endpoint.check_that_status_is_200()
    certain_update_endpoint.check_update_name(body['name'])


def test_delete_object(delete_object, get_object, post_id):
    delete_object.delete_object(post_id)
    delete_object.check_that_status_is_200()
    get_object.get_object(post_id)
    get_object.check_bad_request()
