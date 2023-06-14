from django_filters import FilterSet, CharFilter, DateTimeFilter, ChoiceFilter

from django.forms import DateTimeInput

from .models import Article


class ArticleFilter(FilterSet):
    title_filter = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок'
    )

    added_after = DateTimeFilter(
        field_name='dateArticle',
        lookup_expr='gt',
        widget=DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
        label='Дата публикации позже'
    )
    category = ChoiceFilter(
        field_name='category',
        choices=[(x[0], x[1]) for x in Article.TYPE],
        label='Персонажи',
        empty_label='Все персонажи'
    )
