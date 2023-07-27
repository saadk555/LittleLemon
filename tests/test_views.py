from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        self.menu1 = Menu.objects.create(id=11,title="IceCream", price=80, inventory=101)
        self.menu2 = Menu.objects.create(id=12,title="IceCream", price=80, inventory=102)
    
   
    def test_getall(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        client = Client()
        client.force_login(user)
        response = client.get("http://127.0.0.1:8000/restaurant/menu/")
        serialized_menus = 200
        self.assertEqual(response.status_code, serialized_menus)