from _typeshed import SupportsLessThan
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common import keys
import time

#teste1
class Hosttest(LiveServerTestCase):

    def testhomepage(self):
        driver = webdriver.Chrome()
        
        driver.get('http://127.0.0.1:8000/')

        time.sleep(5)

        assert "Hello world" in driver.title

#teste2
class FormTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/form/')

        time.sleep(4)

        cidade = driver.find_element_by_name('cidade')
        endereço = driver.find_elements_by_name('endereço')
        ano = driver.find_elements_by_name('ano')

        time.sleep(4)

        submit = driver.find_element_by_id('submit')

        cidade.send_keys('Cajazeiras')
        endereço.send_keys('Por do Sol')
        ano.send_keys('2015')

        submit.send_keys(keys.RETURN)

        assert 'Cajazeiras' in driver.page_source