from locust import task, HttpUser
import random


class EndPoints(HttpUser):
    body = None
    post_id = None

    def get_body(self):
        self.body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        return self.body

    @task(10)
    def create_object(self):
        response = self.client.post('/objects', json=self.body)
        self.post_id = response.json()['id']

    @task(3)
    def full_update_object(self):
        body = self.get_body()
        body["data"]["price"] = 2049.99
        body["data"]["color"] = "silver"
        self.client.put(f'/objects/{self.post_id}', json=body)

    @task(2)
    def certain_update_object(self):
        body = self.get_body()
        body["name"] = "Apple MacBook Pro 16 (Updated Name)"
        self.client.patch(f'/objects/{self.post_id}', json=body)

    @task(1)
    def delete_object(self):
        self.client.delete(f'/objects/{self.post_id}')
