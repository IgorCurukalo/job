from django import forms
from app.projects.models import Project
from app.projects.validators import validation_project_name


class ProjectUpdateForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        min_length=2,
        validators=[validation_project_name],
        label='Название проекта',
        widget=forms.TextInput()
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link']
        widgets = {
            'description': forms.Textarea(),
        }

class ProjectUpdateFormAvatar(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['image']