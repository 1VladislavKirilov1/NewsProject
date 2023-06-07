from django_filters import FilterSet, DateTimeFilter, CharFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Category


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    post_category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True
    )
    post_title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title'
    )


