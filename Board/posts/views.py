from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    model = Article
    ordering = 'category'
    template_name = 'posts.html'
    context_object_name = 'posts'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'post.html'
    context_object_name = 'post'