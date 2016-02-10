from django.test import TestCase
from url_shortener.models import URLMap


class BaseTestCase(TestCase):

    def test_the_tests(self):
        URLMap.objects.create(
            original_url="http://someplacenice.co.uk")
