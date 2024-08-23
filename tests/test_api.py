
from backend import app
import unittest
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestAPI(unittest.TestCase):

    def test_api_error(self):
        client = app.test_client()

        resp = client.get('/log', query_string={'entries': 5})
        self.assertEqual(resp.status, '400 BAD REQUEST')
        self.assertEqual(resp.text, 'Bad request. Query param filename: , entries: 5')

        resp = client.get('/log', query_string={'entries': 'aa'})
        self.assertEqual(resp.status, '400 BAD REQUEST')
        self.assertEqual(resp.text, 'Bad request. Query param entries cannot be converted to integer: aa')

        resp = client.get('/log', query_string={'filename': 'NON_EXISTS', 'entries': 3})
        self.assertEqual(resp.status, '400 BAD REQUEST')
        self.assertEqual(resp.text, 'read file failed')
