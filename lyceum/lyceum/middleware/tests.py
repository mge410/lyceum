from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_middlevare_reverse_on_homepage(self):
        client_self = Client()
        print(123)
        for count in range(1, 11):
            response = client_self.get('/')
            if count != 10:
                self.assertContains(
                    response, '<div><h1>Главная страница</h1></div>', status_code=200
                )
            else:
                self.assertContains(
                    response, '<div><h1>яанвалГ ацинартс</h1></div>', status_code=200
                )

    def test_middlevare_reverse_on_catalog(self):
        client_self = Client()
        for count in range(1, 11):
            response = client_self.get('/catalog/')
            if count != 10:
                self.assertContains(
                    response, '<body>Список элементов</body>', status_code=200
                )
            else:
                self.assertContains(
                    response, '<body>косипС вотнемелэ</body>', status_code=200
                )
