from app.views import user_view
from django.http import response
from django.test import TestCase
from django.urls import reverse


class UserViewTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('user_view'))
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(reverse('user_view'))
        self.assertTemplateUsed(response, 'user_view.html')