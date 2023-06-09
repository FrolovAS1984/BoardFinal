from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    authorPost = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=11, choices=TYPE, default=None)
    dateArticle = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])


class UserResponse(models.Model):
    authorComment = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateComment = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text[:20]}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])
