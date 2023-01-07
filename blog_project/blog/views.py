from django.shortcuts import render
from .models import Post, Tag
from django.db.models import Q


def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(body__icontains=search_query)
        )
    else:
        posts = Post.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", context={"tags": tags})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, "blog/post_detail.html", context={"post": post})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, "blog/tag_detail.html", context={"tag": tag})
