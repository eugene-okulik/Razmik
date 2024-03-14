import allure


class Endpoint:
    url = "https://api.restful-api.dev/objects"
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 404 error received')
    def check_bad_request(self):
        assert self.response.status_code == 404

    @allure.step('Check update price in body')
    def check_price_in_body(self, price):
        assert self.response.json()['data']['price'] == price

    @allure.step('Check update name')
    def check_update_name(self, name):
        assert self.response.json()['name'] == name
