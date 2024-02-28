from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class PostIndexView(ListView):
    model = Blog
    template_name = 'blog.html'
    queryset = Blog.objects.all()
    context_object_name  = 'posts' 

class PostDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name  = 'post'  

class BlogsearchView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name  = 'posts'  

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Blog.objects.filter(title__icontains=query).order_by('-created_at')

