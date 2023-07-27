from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(id=11,title="Sandwich", price=90, inventory=99)

    def test_getall(self):
        url = reverse('menu-list')
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        menus = Menu.objects.all()
        expected_data = MenuSerializer(menus, many=True).data
        self.assertEqual(data, expected_data)
