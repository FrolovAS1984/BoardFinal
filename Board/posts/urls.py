from django.urls import path

from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, CommentCreate
from .views import AuthorArticleList, CommentDelete, CommentStatusUpdate

urlpatterns = [
   path('', ArticleList.as_view(), name='post_list'),
   path('<int:pk>', ArticleDetail.as_view(), name='post'),
   path('create/', ArticleCreate.as_view(), name='post_add'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),
   path('<int:pk>/add/', CommentCreate.as_view(), name='comment_add'),
   path('author_articles/', AuthorArticleList.as_view(), name='author_articles'),
   path('comment/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),
   path('comment/<int:pk>/status/', CommentStatusUpdate.as_view(), name='comment_status_update'),


]