import django_filters
from rest_framework import viewsets, serializers
from .models import TestModel


class TestFilter(django_filters.rest_framework.FilterSet):
    first_and_last = django_filters.BooleanFilter(method='first_and_last_filter')

    def first_and_last_filter(self, queryset, name, value):
    	if value==True:
        	return queryset.filter(first=True, last=True);
        return queryset;

    class Meta:
        model = TestModel
        fields = ['first', 'last', 'first_and_last']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['first', 'last']


class TestViewSet(viewsets.ModelViewSet):
    model = TestModel
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('first', 'last', 'first_and_last', )
    filter_class = TestFilter