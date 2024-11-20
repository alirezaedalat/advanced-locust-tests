
import csv
from locust import HttpUser, task, between
from utils.payload_factory import PayloadFactory
from utils.assertions import Assertions

class CompleteTestUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.payload_factory = PayloadFactory()
        self.assertions = Assertions()
        self.users = self.load_users()
        self.token = self.login()

    def load_users(self):
        users = []
        with open("data/users.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users.append(row)
        return users

    def login(self):
        payload = self.payload_factory.create_login_payload(self.users[0])
        response = self.client.post("/auth/login", json=payload)
        self.assertions.assert_status(response, 200)
        return response.json().get("token")

    @task
    def list_crocodiles(self):
        with self.client.get(
            "/public/crocodiles/",
            headers={"Authorization": f"Bearer {self.token}"},
            catch_response=True,
        ) as response:
            self.assertions.assert_status(response, 200)

    @task
    def create_crocodile(self):
        payload = self.payload_factory.create_crocodile_payload()
        with self.client.post(
            "/public/crocodiles/",
            json=payload,
            headers={"Authorization": f"Bearer {self.token}"},
            catch_response=True,
        ) as response:
            self.assertions.assert_status(response, 201)
