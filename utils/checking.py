import json

from requests import Response
"""Method for checking answer"""

class Checking():
    """Method for checking answer code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if status_code == response.status_code:
            print(f"Success! Status code: {str(status_code)}")
        else:
            print(f"Wrong! Status code: {str(status_code)}")


    """Method for checking answer"""

    @staticmethod
    def check_json_code(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All sting are correct")


    """Method for checking required field"""

    @staticmethod
    def check_required_field(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert  check_info == expected_value
        print(f" Correct! '{field_name}' is '{expected_value}'! ")


