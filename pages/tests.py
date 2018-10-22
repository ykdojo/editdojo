from django.test import TestCase


# Create your tests here.
class ApplicationTests(TestCase):
    def test_home_response(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
