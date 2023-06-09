from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Article, UserResponse


class ArticleForm(forms.ModelForm):
    user = None

    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'upload']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Содержание не должно быть идентично заголовку."
            )

        return cleaned_data

    def save(self, commit=True, **kwargs):
        article = super().save(commit=False, **kwargs)
        article.authorPost = self.user
        if commit:
            article.save()
        return article


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['text']
        widgets = {'article': forms.HiddenInput(), 'status': forms.HiddenInput()}

    def save(self, commit=True, **kwargs):
        comment = super().save(commit=False, **kwargs)
        comment.authorComment = self.user
        if commit:
            comment.save()
        return comment
