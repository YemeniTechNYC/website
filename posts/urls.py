from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path("", views.recent_posts, name="recent"),
    path("<int:post_id>/", views.post, name="post"),
]
