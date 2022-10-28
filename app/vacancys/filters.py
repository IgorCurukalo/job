import django_filters
from django import forms
from app.vacancys.models import Vakancys, Busyness
from app.users.models import Skills


class VacancysFilter(django_filters.FilterSet):

    skills_query = Skills.objects.all()
    vakancy_name = django_filters.CharFilter()
    skills = django_filters.ModelMultipleChoiceFilter(queryset=skills_query, widget=forms.CheckboxSelectMultiple())
    busyness_query = Busyness.objects.all()
    busyness = django_filters.ModelChoiceFilter(queryset=busyness_query)

    class Meta:
        model = Vakancys
        fields = ['vakancy_name', 'skills', 'busyness']