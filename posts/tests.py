from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostViewTests(TestCase):
    fixtures = ["posts", "user"]

    def test_no_posts(self):
        Post.objects.all().delete()
        response = self.client.get(reverse("posts:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available")
