from app.models import User
from app.forms import UserForm
from django.test import TestCase

# Create your tests here.
class UserFormTestCase(TestCase):

    def test_user_form_valido(self):
        form = UserForm(data={
            'nome':'Francisco Paulino',
            'idade': 30
        })
        self.assertTrue(form.is_valid())

    def test_user_form_invalido(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())