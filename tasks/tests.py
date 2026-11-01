from django.contrib.auth.models import User
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from django.urls import reverse

from statuses.models import Status
from .models import Label, Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(
            username='miguel',
            password='TestPassword123!',
        )
        self.executor = User.objects.create_user(
            username='ejecutor',
            password='TestPassword123!',
        )
        self.status = Status.objects.create(name='Nuevo')
        self.label = Label.objects.create(name='Urgente')

        self.task = Task.objects.create(
            name='Primera tarea',
            description='Descripción de prueba',
            status=self.status,
            executor=self.executor,
            author=self.author,
        )
        self.task.labels.add(self.label)

    def test_task_list_requires_login(self):
        response = self.client.get(reverse('task_list'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('task_list')}",
        )

    def test_task_list(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.get(reverse('task_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Primera tarea')

    def test_create_task(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('task_create'),
            {
                'name': 'Nueva tarea',
                'description': 'Descripción nueva',
                'status': self.status.pk,
                'executor': self.executor.pk,
                'labels': [self.label.pk],
            },
        )

        self.assertRedirects(response, reverse('task_list'))

        task = Task.objects.get(name='Nueva tarea')
        self.assertEqual(task.author, self.author)
        self.assertEqual(task.executor, self.executor)
        self.assertEqual(task.status, self.status)
        self.assertIn(self.label, task.labels.all())

    def test_update_task(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('task_update', args=[self.task.pk]),
            {
                'name': 'Tarea modificada',
                'description': 'Descripción modificada',
                'status': self.status.pk,
                'executor': self.executor.pk,
                'labels': [self.label.pk],
            },
        )

        self.assertRedirects(response, reverse('task_list'))

        self.task.refresh_from_db()
        self.assertEqual(self.task.name, 'Tarea modificada')
        self.assertEqual(
            self.task.description,
            'Descripción modificada',
        )

    def test_delete_own_task(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('task_delete', args=[self.task.pk])
        )

        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(
            Task.objects.filter(pk=self.task.pk).exists()
        )

    def test_cannot_delete_another_users_task(self):
        User.objects.create_user(
            username='otro',
            password='TestPassword123!',
        )

        self.client.login(
            username='otro',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('task_delete', args=[self.task.pk])
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Task.objects.filter(pk=self.task.pk).exists()
        )

    def test_task_detail(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.get(
            reverse('task_detail', args=[self.task.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Primera tarea')
        self.assertContains(response, 'Urgente')

    def test_cannot_delete_user_with_tasks(self):
        with self.assertRaises(ProtectedError):
            self.author.delete()

        self.assertTrue(
            User.objects.filter(pk=self.author.pk).exists()
        )


class LabelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='miguel',
            password='TestPassword123!',
        )
        self.label = Label.objects.create(name='Urgente')

    def test_label_list_requires_login(self):
        response = self.client.get(reverse('label_list'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('label_list')}",
        )

    def test_label_list(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.get(reverse('label_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Urgente')

    def test_create_label(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('label_create'),
            {'name': 'Mejora'},
        )

        self.assertRedirects(response, reverse('label_list'))
        self.assertTrue(
            Label.objects.filter(name='Mejora').exists()
        )

    def test_update_label(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('label_update', args=[self.label.pk]),
            {'name': 'Bug'},
        )

        self.assertRedirects(response, reverse('label_list'))

        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Bug')

    def test_delete_label(self):
        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('label_delete', args=[self.label.pk])
        )

        self.assertRedirects(response, reverse('label_list'))
        self.assertFalse(
            Label.objects.filter(pk=self.label.pk).exists()
        )

    def test_cannot_delete_label_associated_with_task(self):
        status = Status.objects.create(name='Nuevo')
        task = Task.objects.create(
            name='Tarea de prueba',
            description='Descripción',
            status=status,
            executor=self.user,
            author=self.user,
        )
        task.labels.add(self.label)

        self.client.login(
            username='miguel',
            password='TestPassword123!',
        )

        response = self.client.post(
            reverse('label_delete', args=[self.label.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Label.objects.filter(pk=self.label.pk).exists()
        )
        self.assertContains(
            response,
            'No se puede eliminar una etiqueta asociada a una tarea.',
        )
