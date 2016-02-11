from django.test import TestCase
from url_shortener.models import URLMap


class BaseTestCase(TestCase):

    def test_URLMap_model(self):
        URLMap.objects.create(
            original_url="http://someplacenice.co.uk")
        self.assertEqual(
            len(URLMap.objects.get(id=1).shortcode), 8)
