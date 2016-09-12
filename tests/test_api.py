import unittest
from context import API


class TestAPIMethods(unittest.TestCase):

    def setUp(self):
        self.uid = None
        self.config = {'token': '',
                       'appname': 'Python API Testing Application',
                       'device': 'terminal/library',
                       'version': '0.1.1'}

    def test_websites_ok(self):
        api = API(self.config)
        response = api.websites().get_raw()
        self.assertEqual(response['status'], 'ok')

    def test_website_ok(self):
        api = API(self.config)
        response = api.website(163).get_raw()
        self.assertEqual(response['status'], 'ok')

    def test_balance_ok(self):
        api = API(self.config)
        response = api.balance().get_raw()
        self.assertEqual(response['status'], 'ok')

    def test_user_ok(self):
        api = API(self.config)
        response = api.user().get_raw()
        self.assertEqual(response['status'], 'ok')

    def test_credits_ok(self):
        api = API(self.config)
        response = api.credits().get_raw()
        self.assertEqual(response['status'], 'ok')

    def test_submit_crawl_ok(self):
        api = API(self.config)
        response = api.create('http://passmarked.com')
        self.uid = str(response.get('uid'))
        self.assertEqual(response.get_raw()['status'], 'ok')

        response = api.get(self.uid).get_raw()
        self.assertEqual(response['status'], 'ok')

    def test_submit_ok(self):
        api = API(self.config)
        response = api.submit('https://passmarked.com').get_raw()
        self.assertEqual(response['status'], 'ok')

if __name__ == '__main__':
    unittest.main()
