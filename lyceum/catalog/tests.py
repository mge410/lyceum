from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_list_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_detail_endpoint(self):
        response = Client().get('/catalog/123')
        self.assertEqual(response.status_code, 200)

    def test_bad_catalog_detail_endpoint(self):
        response = Client().get('/catalog/sfd')
        self.assertEqual(response.status_code, 404)

    def test_catalog_detail_re_endpoint(self):
        response = Client().get('/catalog/re/1')
        self.assertEqual(response.status_code, 200)

    def test_bad_catalog_detail_re_endpoint(self):
        response = Client().get('/catalog/re/dfg')
        self.assertEqual(response.status_code, 404)

    def test_catalog_detail_converter_endpoint(self):
        response = Client().get('/catalog/converter/1')
        self.assertEqual(response.status_code, 200)

    def test_bad_catalog_detail_converter_endpoint(self):
        response = Client().get('/catalog/converter/dfg')
        self.assertEqual(response.status_code, 404)
