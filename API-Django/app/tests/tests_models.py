from django.test import TestCase
from ..models import User
# Create your tests here.

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            nome = 'Francisco Paulino',
            idade = 30
        )
    def test_retorno_str(self):
        p1 = User.objects.get(nome='Francisco Paulino')
        self.assertEquals(p1.__str__(), 'Francisco Paulino')

        