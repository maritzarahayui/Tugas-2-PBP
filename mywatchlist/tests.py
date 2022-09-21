from django.test import TestCase
from django.test import Client

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_mywatchlist(self):
        response = Client().get('/mywatchlist')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist(self):
        response = Client().get('/mywatchlist/xtml/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
