from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Blogs

# Create your views here.
def index(request): 

    posts = Blogs.objects.order_by('-created_at')[:10]

    context = {
        'posts' : posts
    }

    return render(request, 'blogs/index.html', context)

# Details Posts
def detail(request, post_id):
    try:
        post = Blogs.objects.get(pk=post_id)
    except Blogs.DoesNotExist:
        raise Http404("Questions does not exist")
    return render(request, 'blogs/detail.html', { 'post': post })
