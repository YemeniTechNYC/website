from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    image_url = models.CharField(max_length=100, null=True)
    body = models.TextField(null=False)
    pub_date = models.DateTimeField("date published", null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
