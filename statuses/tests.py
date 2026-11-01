
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Status


class StatusTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='miguel',
            password='TestPassword123!',
        )
        self.status = Status.objects.create(name='Nuevo')

    def test_status_list_requires_login(self):
        response = self.client.get(reverse('status_list'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('status_list')}",
        )

    def test_status_list(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.get(reverse('status_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nuevo')

    def test_create_status(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('status_create'),
            {'name': 'En progreso'},
        )

        self.assertRedirects(response, reverse('status_list'))
        self.assertTrue(
            Status.objects.filter(name='En progreso').exists()
        )

    def test_update_status(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('status_update', args=[self.status.pk]),
            {'name': 'Terminado'},
        )

        self.assertRedirects(response, reverse('status_list'))

        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Terminado')

    def test_delete_status(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('status_delete', args=[self.status.pk])
        )

        self.assertRedirects(response, reverse('status_list'))
        self.assertFalse(
            Status.objects.filter(pk=self.status.pk).exists()
        )
