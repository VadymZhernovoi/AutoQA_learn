import json

import requests


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_employee(self, employee_id):
        resp = requests.get(self.url + '/employee/info/' + str(employee_id))
        assert resp.status_code == 200
        return resp.json()

    def get_token(self, user, password):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200
        return resp.json()["user_token"]

    # Create company
    def create_employee(self, employee):
        resp = requests.post(self.url + '/employee/create', json=employee)
        assert resp.status_code == 200
        return resp.json()

    # Update company
    def update_employee(self, id, changed):
        client_token = self.get_token("harrypotter", "expelliarmus")
        url_with_token = self.url + "/employee/change/" + str(id) + "?client_token=" + client_token
        resp = requests.patch(url_with_token, json=changed)

        assert resp.status_code == 200

        return resp.json()