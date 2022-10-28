from django.urls import reverse
from rest_framework import status
from django.test import Client

from rest_framework.test import APITestCase
from apps.books.models import PublishingHouse


class PublishingHouseGetTestCase(APITestCase):
    def test_publishing_house_get(self):
        response = self.client.get('/books/publishing_house/1/')
        self.assertEqual(response.data, {'id': '1', 'publishing_house_name': 'Тюмень, Минская, 33'}, status.HTTP_200_OK)


class PublishingHousePostTestCase(APITestCase):
    def test_publishing_house_post(self):
        data = {
            'publishing_house_name': 'Дом милый дом',
            'adress': 'Малыгина 84 кв 66',
            'contact_phone': '123423423424',
            'email': '123@ya.ru',
            'website_linck': 'https://127.0.0.1:8000'
        }
        response = self.client.post('/books/publishing_house/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
