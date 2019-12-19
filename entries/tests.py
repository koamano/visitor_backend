from django.test import TestCase
from .models import Entries
from .urls import *

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    def setUp(self):
        self.entry_name = "test name"
        self.entry_note = "test note"
        self.entry = Entries(name=self.entry_name, notes=self.entry_note, is_signout=True)

    def test_model_create(self):
        self.entry.save()
        count = Entries.objects.count()
        self.assertEqual(1,count)

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.entry_data = {'name': 'view name', 'notes': 'view test notes', 'is_signout':False}
        self.response = self.client.post(
            '/api/entries/',
            self.entry_data,
            format="json")

    def test_api_can_create(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get(self):
        entryList = Entries.objects.get()
        response = self.client.get(
            '/api/entries/',
            format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, entryList)

    def test_api_can_update(self):
        change_entry = {'name': 'Something new', 'notes': 'a new note'}
        res = self.client.put(
            '/api/entries/1/',
            change_entry, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        

