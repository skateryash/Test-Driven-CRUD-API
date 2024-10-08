import json
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .models import Item

class ItemAPITestCase(TestCase):

    def setUp(self):
        self.item = Item.objects.create(name='test item', description = 'This is a test item')

    def test_get_item_list(self):
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_item(self):
        url = reverse('item-detail', kwargs={'id':self.item.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_create_item(self):
        url = reverse('item-create')
        data = {"name": "Vada Pav", "description": "This is a famous Mumbai item"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)

    def test_update_item(self):
        url = reverse('item-update', kwargs={'id': self.item.id})
        data = {"name": "Updated name", "description": "Updated item description"}
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated name')

    def test_delete_item(self):
        url = reverse('item-delete', kwargs={'id': self.item.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)
