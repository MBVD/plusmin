import django_filters
from .models import *
from django_filters import DateFilter, NumberFilter,RangeFilter, OrderingFilter

class RatingFilter(django_filters.FilterSet):
    rate = OrderingFilter(fields=('rate', 'rate'), field_labels = {'rate': 'Рейтинг'})
    class Meta:
        model = UserProfile
        fields = ['rate', 'country']

class ProblemsFilters(django_filters.FilterSet):
    rate = OrderingFilter(fields = ('rate', 'rate'), field_labels = {'rate': "Рейтинг"})
    class Meta:
        model = Problem
        fields = ['rate']