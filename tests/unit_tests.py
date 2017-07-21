"""
This test cases will be used to test if the client api is working
"""
import unittest
from ..flask_api import APP


class TestAPITestCases(unittest.TestCase):
    def setUp(self):
        """
        Initial configuration
        :return: self.app
        """
        self.app = APP.test_client()

    def test_specific_bucket_list(self):
        """
        Test get bucket list with invalid key
        Test get bucket with a valid key
        :return: status code
        """
        response = self.app.get('/bucketlist/api/v1.0/bucketlists/22222222')
        self.assertEqual(response.status_code, 404)
        response = self.app.get('/bucketlist/api/v1.0/bucketlists/00000000')
        self.assertEqual(response.status_code, 200)
