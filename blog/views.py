# Create your views here.
from models import Post
from django.shortcuts import render

def blog_post(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = "post_list.html"

    context = {
        "post_list": post_list
    }

    return render(request, template_name, context)

def blog_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk, published=True)
    template_name = "post_detail.html"

    context = {
        "post": post
    }

    return render(request, template_name, context)