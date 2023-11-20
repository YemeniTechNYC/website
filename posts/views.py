from django.shortcuts import get_object_or_404, render

from .models import Post


def recent_posts(request):
    page = request.GET.get("page", 1)
    LIMIT = 10
    offset = (page - 1) * LIMIT
    posts = Post.objects.order_by("-pub_date")[offset : offset + LIMIT]
    context = {"latest_posts": posts}
    return render(request, "posts/index.html", context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "posts/detail.html", {"post": post})
