from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.

class UserTest(APITestCase):
    url = reverse('user-list')
    data = { 'username' : 'kay',
             'email': ''}
