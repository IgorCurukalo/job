import django_filters
from django import forms
from app.users.models import Profile, Skills
from app.msg.models import Msg


class ProfileFilter(django_filters.FilterSet):

    skills_query = Skills.objects.all()
    profile_name = django_filters.CharFilter()
    skills = django_filters.ModelMultipleChoiceFilter(queryset=skills_query, widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Profile
        fields = ['profile_name', 'skills']