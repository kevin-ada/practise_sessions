import unittest
import requests


class TestRequests(unittest.TestCase):
    def test_get_request(self):
        response = requests.get('https://httpbin.org/get')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        parameters = {'username': 'kimCodes', 'Password': 'jibbrish'}
        response = requests.post('https://httpbin.org/post', json=parameters)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
