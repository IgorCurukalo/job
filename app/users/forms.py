from django import forms
from django.contrib.auth.models import User
from app.users.models import Profile, Skills
from app.users.validators import validation_profile_name

#форма логирования
class LoginForm(forms.Form):

    username = forms.CharField(max_length=250, label='Логин', )
    password = forms.CharField(label='Пароль', )

    class Meta:
        model = User
        fields = ('username', 'password')

#форма регистрации
class RegistrationForm(forms.Form):

    first_name = forms.CharField(max_length=250, label='Имя', )
    last_name = forms.CharField(max_length=250, label='Фамилия', )
    email = forms.EmailField(label='email', )

    username = forms.CharField(max_length=250, label='Имя используемое при авторизации', )

    password = forms.CharField(label='Пароль', )
    password2 = forms.CharField(label='Подтвердите пароль', )

    class Meta:
        model = User

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

#форма обновления юзера
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']

#форма обновления профиля
class ProfileUpdateForm(forms.ModelForm):

    profile_name = forms.CharField(
        required=True,
        min_length=2,
        validators=[validation_profile_name],
        label='Название профиля/организации',
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
        model = Profile
        fields = ['profile_name', 'tel', 'skills', 'id_type_user', 'adr', 'biog', 'github', 'twitter', 'youtube', 'website']
        exclude = ['projects']
        widgets = {
            'biog': forms.Textarea(),
            'skills': forms.CheckboxSelectMultiple(),
        }

#форма обвновления профиля аватара
class ProfileUpdateFormAvatar(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']