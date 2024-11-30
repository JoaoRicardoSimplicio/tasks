import factory

from django.urls import reverse
from factory.django import DjangoModelFactory
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task


class TestTask(APITestCase):

    def test_create_task(self):
        url = reverse("task-list-create")
        data = {
            "title": "Test 1",
            "description": "Task made to test create endpoint"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_list_tasks(self):
        TaskFactory.create_batch(5)

        url = reverse("task-list-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_delete_task(self):
        task = TaskFactory.create()

        url = reverse("task-retrieve-update-delete", kwargs={"pk": task.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_update_task(self):
        task = TaskFactory.create(
            title = "Test 1",
            description = "Task made to test create endpoint"
        )

        new_description = "Task made to test update endpoint"

        url = reverse("task-retrieve-update-delete", kwargs={"pk": task.id})
        response = self.client.patch(url, data={"description": new_description})

        task.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task.description, new_description)

    def test_set_task_as_done(self):
        task = TaskFactory.create()

        self.assertEqual(task.status, "Todo")

        url = reverse("task-set-as-complete", kwargs={"pk": task.id})
        response = self.client.post(url)


        task.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task.status, "Done")
