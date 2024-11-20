
class PayloadFactory:
    def create_login_payload(self, user):
        return {
            "username": user["username"],
            "password": user["password"],
        }

    def create_crocodile_payload(self):
        return {
            "name": "CrocTest",
            "age": 5,
            "gender": "M",
        }
