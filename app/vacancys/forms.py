from django import forms
from app.vacancys.models import Vakancys
from app.vacancys.validators import validation_vak_name
from app.users.models import Skills


#форма обновления вакансии
class VakancysUpdateForm(forms.ModelForm):

    skills_query = Skills.objects.all()
    skills_query = [
        (skills.id, skills.skills_name) for skills in skills_query
    ]
    skills = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=skills_query,
        initial=True,
        required=True,
        label='Скиллы'
    )

    class Meta:
        model = Vakancys
        fields = ['vakancy_name', 'salary', 'description', 'tasks', 'experience', 'busyness', 'skills']
        widgets = {
            'description': forms.Textarea(),
            'tasks': forms.Textarea(),
        }


#форма новой вакансии
class VakancysAddForm(forms.ModelForm):

    vakancy_name = forms.CharField(
        required=True,
        min_length=2,
        validators=[validation_vak_name],
        label='Название вакансии',
        widget=forms.TextInput()
    )

    skills_query = Skills.objects.all()
    skills_query = [
        (skills.id, skills.skills_name) for skills in skills_query
    ]
    skills = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=skills_query,
        required=True,
        label='Скиллы'
    )

    class Meta:
        model = Vakancys
        fields = ['vakancy_name', 'salary', 'description', 'tasks', 'experience', 'busyness', 'skills']
        widgets = {
            'description': forms.Textarea(),
            'tasks': forms.Textarea(),
        }