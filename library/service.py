from django_filters import rest_framework as filters
from library.models import Book


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    title = CharFilterInFilter(field_name='title', lookup_expr='in')
    category = CharFilterInFilter(field_name='category', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = Book
        fields = ['title', 'category']