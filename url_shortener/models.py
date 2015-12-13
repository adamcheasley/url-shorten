import hashlib
from django.db import models


class URLMap(models.Model):
    """Map a shortened URL to the original URL
    """
    original_url = models.TextField()
    shortcode = models.CharField(max_length=255, editable=False)

    def save(self):
        self.shortcode = hashlib.sha256(
            self.original_url.encode('ascii')).hexdigest()[:8]
        super(URLMap, self).save()
