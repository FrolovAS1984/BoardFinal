from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, UserResponse
from .forms import ArticleForm, CommentForm
from django.urls import reverse_lazy


class ArticleList(ListView):
    model = Article
    ordering = '-dateArticle'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5


class AuthorArticleList(LoginRequiredMixin, ListView):
    model = Article
    ordering = '-dateArticle'
    context_object_name = 'articles'
    template_name = 'author_articles.html'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(authorPost=self.request.user)


class ArticleDetail(DetailView):
    model = Article
    template_name = 'post.html'
    context_object_name = 'post'


class ArticleCreate(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    model = Article
    template_name = 'post_add.html'

    def form_valid(self, form):
        form.user = self.request.user  # передаем текущего пользователя в форму
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'post_add.html'

    def form_valid(self, form):
        form.user = self.request.user  # передаем текущего пользователя в форму
        return super().form_valid(form)


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CommentCreate(CreateView):
    form_class = CommentForm
    model = UserResponse
    template_name = 'comment_add.html'

    def form_valid(self, form):
        form.user = self.request.user
        # Получаем объект комментария, которые заполнил пользователь
        response = form.save(commit=False)
        # Находим объект объявления, которому был оставлен комментарий
        article = Article.objects.get(pk=self.kwargs['pk'])
        # Сохраняем этот объект и устанавливаем соответствующее значение поля
        # article с помощью созданного ранее скрытого поля
        response.article = article
        response.save()
        form.save_m2m()
        # Наконец, делаем редирект к странице, на которой был оставлен комментарий
        return redirect(article.get_absolute_url())


class CommentDelete(DeleteView):
    model = UserResponse
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('author_articles')

