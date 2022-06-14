from django.test import Client, TestCase
from django.urls import reverse


class ViewTestCase(TestCase):

    def test_example_view(self):
        client = Client()
        language_code = 'pt-BR'
        resp = client.get(reverse('example'), HTTP_ACCEPT_LANGUAGE=language_code)
        received = resp.json()['language_code']
        assert received == language_code, f'{received} != {language_code}'
        # ^-- AssertionError: pt != pt-BR
