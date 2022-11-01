from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json
from app.users.models import Profile, User
from app.projects.models import Project
from app.vacancys.models import Vakancys
from app.msg.models import Msg


#тест создания пользователя, логирования
class CreateUserTestCase(APITestCase):

    def test_create_user(self):
        data = {'username': 'testcase', 'email': 'testcase@mail.ru', 'password': 'admin', 'password2': 'admin'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        data = {'username': 'admin', 'password': 'admin'}
        self.client.login(username=data['username'], password=data['password'])
        response = self.client.get(reverse('logout'), data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)


#тест главной страницы
class IndexTestCase(APITestCase):

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#тест главной страницы
class InboxTestCase(APITestCase):

    def test_inbox(self):
        response = self.client.get(reverse('inbox'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#тест User,Profile,Project,Vacancy,
class ProfileTestCase(APITestCase):

    def test_profile(self):
        self.u = User.objects.create(
            username='testcase', email='testcase@mail.ru', password='admin', password2='admin')
        self.p = Profile.objects.create(
            user=self.u.pk, profile_name='Casper', tel=3, skills='python',
            id_type_user=1, adr='Тюмень ул.Миротворцев 1', biog='Супер программист',
            image='profile_images/default.jpg', github='', twitter='', youtube='', website='')
        self.uc = User.objects.create(
            username='testcasecom', email='testcasecom@mail.ru', password='admin', password2='admin')
        self.pc = Profile.objects.create(
            user=self.u.pk, profile_name='Casper', tel=3, skills='python',
            id_type_user=2, adr='Тюмень ул.Миротворцев 1', biog='Супер компания',
            image='profile_images/default.jpg', github='', twitter='', youtube='', website='')

    def test_projects(self):
        self.pr = Project.objects.create(
            user=self.u.pk, title='KFC', image='profile_project/default.jpg',
            description='курочка в соусе', demo_link='-'
        )

    def test_vacancys(self):
        self.vk = Vakancys.objects.create(
            profile=self.pc, vakancy_name='Super python', salary='100000 руб', description='Супер проект',
            tasks='Выполниять все задачи', adr='Тюмень ул.Мира 3', experience='1 год',
            busyness=1, skills='python', count='0')

    def test_user_account(self):
        response = self.client.get(
            reverse('profile_user', kwargs={'pk': self.p.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_account(self):
        response = self.client.put(
            reverse('editAccount', kwargs={'pk': self.u.pk}),
            data=json.dumps(self.u, self.p),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_project_detail(self):
        response = self.client.get(
            reverse('project', kwargs={'pk': self.pr.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vacancy_detail(self):
        response = self.client.get(
            reverse('vacancy', kwargs={'pk': self.vk.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_prog_detail(self):
        response = self.client.get(
            reverse('profile_detail_prog', kwargs={'pk': self.p.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_com_detail(self):
        response = self.client.get(
                reverse('profile_detail_com', kwargs={'pk': self.pc.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_prog(self):
        response = self.client.get(reverse('программист'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_com(self):
        response = self.client.get(reverse('компания'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_projects(self):
        response = self.client.put(
            reverse('editProject', kwargs={'pk': self.pr.pk}),
            data=json.dumps(self.pr),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_edit_vacancys(self):
        response = self.client.put(
            reverse('editVacancy', kwargs={'pk': self.vk.pk}),
            data=json.dumps(self.vk),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_msg_create(self):
        data = {'sender': self.p.pk, 'recipient': self.pc.pk, 'name_msg': 'Тема', 'body': 'Текст сообщения'}
        response = self.client.post(reverse('create-msg'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_msg_add(self):
        self.ms = Msg.objects.create(
            sender=self.p.pk, recipient=self.pc.pk,
            name_msg='Тема',body='Текст сообщения'
        )

    def test_msg(self):
        response = self.client.get(
            reverse('msg', kwargs={'pk': self.ms.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_account(self):
        response = self.client.delete(
            reverse('delete-msg', kwargs={'pk': self.ms.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_projects(self):
        response = self.client.delete(
            reverse('deleteProject', kwargs={'pk': self.pr.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_vacancys(self):
        response = self.client.delete(
            reverse('deleteVacancy', kwargs={'pk': self.vk.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_account(self):
        response = self.client.delete(
            reverse('deleteAccount', kwargs={'pk': self.u.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#тест подвала сайта
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