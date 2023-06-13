from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import UserResponse


@receiver(post_save, sender=UserResponse)
def comment_created(instance, created, **kwargs):
    if not created:
        return

    article = instance.article
    author = article.authorPost

    subject = f'Новый комментарий к объявлению "{article.title}"'

    text_content = (
        f'Пользователь {instance.authorComment.username} оставил комментарий к вашему объявлению "{article.title}"\n\n'
        f'Ссылка на Вашу приватную страницу: http://127.0.0.1:8000/posts/author_articles/'
    )
    html_content = (
        f'<p>Пользователь {instance.authorComment.username} оставил комментарий к вашему объявлению "{article.title}"</p>'
        f'<p><a href="http://127.0.0.1:8000/posts/author_articles/">Ссылка на Вашу приватную страницу</a></p>'
    )

    msg = EmailMultiAlternatives(subject, text_content, None, [author.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(post_save, sender=UserResponse)
def comment_created(instance, created, **kwargs):
    if not instance.status:
        return

    article = instance.article
    author = instance.authorComment

    subject = f'Подтверждение комментария к объвлению "{article.title}"'

    text_content = (
        f'Подтвержден комментарий "{instance.text}"'
    )
    html_content = (
        f'Подтвержден комментарий "{instance.text}"'
       )

    msg = EmailMultiAlternatives(subject, text_content, None, [author.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(pre_delete, sender=UserResponse)
def notify_comment_author(sender, instance, **kwargs):
    email = instance.authorComment.email
    article_title = instance.article.title
    subject = f'Отклонение комментария к объвлению "{article_title}"'
    text_content = (
        f'Удален комментарий "{instance.text}" к объявлению "{article_title}"'
    )
    html_content = (
        f'Удален комментарий "{instance.text}" к объявлению "{article_title}"'
    )

    msg = EmailMultiAlternatives(subject, text_content, None, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
