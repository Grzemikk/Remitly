import json


def verify_json_input(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        statements = data['PolicyDocument']['Statement']
        for statement in statements:
            if statement['Resource'] == '*':
                return False
        return True
    except (KeyError, json.JSONDecodeError) as e:
        return False

print(verify_json_input('false.json'))
print(verify_json_input('wrongFormat.json'))
print(verify_json_input('true.json'))

import unittest

class TestVerifyJsonInput(unittest.TestCase):
    def test_with_asterisk(self):
        result = verify_json_input('false.json')
        self.assertFalse(result)
        print(result)

    def test_no_resource_field(self):
        result = verify_json_input('wrongFormat.json')
        self.assertFalse(result)
        print(result)

    def test_without_asterisk(self):
        result = verify_json_input('true.json')
        self.assertTrue(result)
        print(result)   



if __name__ == '__main__':
    unittest.main()