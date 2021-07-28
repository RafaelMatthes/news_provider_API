from .test_models import ModelBase
from rest_framework.test import force_authenticate, APIClient
from portal.models import *
from django.urls import reverse
from rest_framework import status

class ViewSetsTestCase(ModelBase):

    def test_user_viewset(self):
        data = {
                    "username":"Tester",
                    "password":"123123",
                    "email" : "test2@mail.com"
                }
        
        list_url = reverse('Signup-list')

        response = self.client.post(list_url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_user_viewset_invalid_data(self):
        data = {
                    "username":"",
                    "password":"",
                    "email" : "test2@mail.com"
                }
        
        list_url = reverse('Signup-list')

        response = self.client.post(list_url, data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_author_viewset_unauthorized(self):
        
        list_url = reverse('Authors-list')

        response = self.client.get(list_url, AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(response, user=self.user)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)



    

