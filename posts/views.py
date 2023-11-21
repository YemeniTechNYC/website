from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = "posts/index.html"
    context_object_name = "latest_posts"
    model = Post
    paginate_by = 2
    ordering = ["-pub_date"]


class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/detail.html"
