from django.test import TestCase

from models import Sales
# Create your tests here.

class SalesTestCase(TestCase):
    def setUp(self):
        Sales.objects.create(
            cidade='Cachoeira dos Indios',
            endereço='sitio lagoa do mato',
            ano=2015
        )

    def test_retorno_str(self):
        p1 = Sales.objects.get(cidade='Cachoeira dos Indios')
        self.assertEquals(p1.__Str__(), 'Cachoeira')