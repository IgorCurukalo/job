from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CreateUserTestCase(APITestCase):

    def test_create_user(self):
        data = {'username': 'testcase', 'email': 'testcase@mail.ru', 'password': 'admin', 'password2': 'admin'}
        response = self.client.post('/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_login(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        data = {'username': 'admin', 'password': 'admin'}
        self.client.login(username=data['username'], password=data['password'])
        response = self.client.get('/logout/', data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

class FooterTestCase(APITestCase):

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_security(self):
        response = self.client.get(reverse('security'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)