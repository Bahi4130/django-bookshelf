import django_filters


class BookFilter(django_filters.FilterSet):

    isbn = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    borrowed_by_who = django_filters.CharFilter(lookup_expr='icontains')
    is_borrowed = django_filters.BooleanFilter()
