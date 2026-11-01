
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserCreateTest(TestCase):
    def test_create_user(self):
        response = self.client.post(
            reverse('user_create'),
            {
                'first_name': 'Miguel',
                'last_name': 'Joya',
                'username': 'miguel',
                'password1': 'TestPassword123!',
                'password2': 'TestPassword123!',
            },
        )

        self.assertRedirects(response, reverse('login'))
        self.assertTrue(
            User.objects.filter(username='miguel').exists()
        )


class UserUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='miguel',
            password='TestPassword123!',
            first_name='Miguel',
            last_name='Joya',
        )

    def test_update_own_user(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('user_update', args=[self.user.pk]),
            {
                'first_name': 'Miguel Angel',
                'last_name': 'Joya',
                'username': 'miguel',
            },
        )

        self.assertRedirects(response, reverse('users'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Miguel Angel')

    def test_cannot_update_another_user(self):
        another_user = User.objects.create_user(
            username='otro',
            password='TestPassword123!',
        )

        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('user_update', args=[another_user.pk]),
            {
                'first_name': 'Cambio',
                'last_name': 'No permitido',
                'username': 'otro',
            },
        )

        self.assertEqual(response.status_code, 403)

        another_user.refresh_from_db()
        self.assertEqual(another_user.first_name, '')


class UserDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='miguel',
            password='TestPassword123!',
        )

    def test_delete_own_user(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('user_delete', args=[self.user.pk])
        )

        self.assertRedirects(response, reverse('users'))
        self.assertFalse(
            User.objects.filter(pk=self.user.pk).exists()
        )

    def test_cannot_delete_another_user(self):
        another_user = User.objects.create_user(
            username='otro',
            password='TestPassword123!',
        )

        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('user_delete', args=[another_user.pk])
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            User.objects.filter(pk=another_user.pk).exists()
        )
