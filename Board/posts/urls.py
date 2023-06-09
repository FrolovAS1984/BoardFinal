from django.urls import path

from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, CommentCreate, AuthorArticleList,CommentDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', ArticleList.as_view(), name='post_list'),
   path('<int:pk>', ArticleDetail.as_view(), name='post'),
   path('create/', ArticleCreate.as_view(), name='post_add'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),
   path('<int:pk>/add/', CommentCreate.as_view(), name='comment_add'),
   path('author_articles/', AuthorArticleList.as_view(), name='author_articles'),
   path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete')
]