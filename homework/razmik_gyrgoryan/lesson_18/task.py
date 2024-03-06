import requests


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
    assert res.status_code == 200, "Status code error"
    assert res.json()['id'] == 7, 'Id is incorrect'
    return res.json()['id']


def clear(post_id):
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')


def full_update_object():
    post_id = create_object()
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
    res = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=body, headers=headers)
    assert res['data']['price'] == 2049.99
    clear(post_id)


def certain_update_object():
    post_id = create_object()
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {"content-type": "application/json"}
    res = requests.patch(f"https://api.restful-api.dev/objects/{post_id}", json=body, headers=headers)
    assert res['name'] == "Apple MacBook Pro 16 (Updated Name)"
    clear(post_id)


def delete_object():
    res = requests.delete("https://api.restful-api.dev/objects/6")
    return res.status_code, res.json()
