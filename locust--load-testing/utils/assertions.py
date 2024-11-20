
class Assertions:
    def assert_status(self, response, expected_status):
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

    def assert_key_in_response(self, response, key):
        assert key in response.json(), f"Key '{key}' not found in response"
