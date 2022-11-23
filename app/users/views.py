from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django.views.generic import DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from app.users.forms import RegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm, ProfileUpdateFormAvatar
from app.users.models import Profile
from app.projects.models import Project
from app.vacancys.models import Vakancys
from app.msg.models import Msg
from app.users.filters import ProfileFilter
from app.users.count import countVacancys, countProfileProg, countProfileCom

#Создание пользователя
def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user = User(**form.cleaned_data)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
        return redirect('login')
    else:
        form = RegistrationForm()
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/registration.html', context=context)

#авторизация пользователя
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('profile')
            else:
                messages.success(request, f'Не верный логин/пароль')
    else:
        form = LoginForm()
    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)

#отключение пользователя
def logout_user(request):
    auth.logout(request)
    return redirect('index')

#просмотр профиля авторизованного пользователя для заполнения реквизитов
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        p_form_avatar = ProfileUpdateFormAvatar(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and p_form_avatar.is_valid():
            u_form.save()
            p_form.save()
            p_form_avatar = p_form_avatar.save(commit=False)
            p_form_avatar.user = request.user.profile.user
            p_form_avatar.save()
            return redirect('index')
    else:
        if request.user.profile.image == 'profile_images/default.jpg':
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            p_form_avatar = ProfileUpdateFormAvatar(instance=request.user.profile)
        else:
            return redirect('index')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'p_form_avatar': p_form_avatar,
    }
    return render(request, 'users/profile.html', context)

#просмотр акаунта пользователя (профиль + проекты/вакансии)
def userAccount(request):
    profile = request.user.profile
    projects = Project.objects.filter(user=request.user)
    vacancys = Vakancys.objects.filter(profile=request.user.profile)
    messageRecipient = Msg.objects.filter(recipient=profile)
    unreadCount = f'({messageRecipient.filter(is_read=False).count()})'
    context = {'profile': profile,
               'projects': projects,
               'vacancys': vacancys,
               'unreadCount': f'({Msg.objects.filter(recipient=profile, is_read=False).count()})'
               }
    return render(request, 'users/profile_account.html', context)

#изменение аккаунта пользователя
def editAccount(request):
    profile = request.user.profile
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        p_form_avatar = ProfileUpdateFormAvatar(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and p_form_avatar.is_valid():
            u_form.save()
            p_form.save()
            p_form_avatar = p_form_avatar.save(commit=False)
            p_form_avatar.user = request.user.profile.user
            p_form_avatar.save()
            return redirect('profile')
    else:
        if request.user.profile.image != 'profile_images/default.jpg':
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            p_form_avatar = ProfileUpdateFormAvatar(instance=request.user.profile)
        else:
            return redirect('profile')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'p_form_avatar': p_form_avatar,
        'unreadCount': f'({Msg.objects.filter(recipient=profile, is_read=False).count()})'
    }
    return render(request, 'users/profile.html', context)


#Список профилей-компаний
class ProfileListCom(FilterView):
    model = Profile
    filterset_class = ProfileFilter
    context_object_name = 'profile'
    template_name = 'users/profile_list.html'
    queryset = Profile.objects.filter(id_type_user__type_user_name='компания')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProfileListCom, self).get_context_data(**kwargs)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


#Список профилей-программистов
class ProfileListProg(FilterView):
    model = Profile
    filterset_class = ProfileFilter
    context_object_name = 'profile'
    template_name = 'users/profile_list.html'
    queryset = Profile.objects.filter(id_type_user__type_user_name='программист')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProfileListProg, self).get_context_data(**kwargs)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


#детализация профиля пользователя
class ProfileDetail(DetailView):
    model = Profile
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(user=self.object.user)
        context['vacancys'] = Vakancys.objects.filter(profile=self.object.user.profile)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


# удаление пользователя
class DeleteAccount(DeleteView):
    model = User
    template_name = 'users/profile_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(DeleteAccount, self).get_context_data(**kwargs)
        context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        return context


#главная страница
class Index(ListView):
    model = Profile
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profilecom'] = Profile.objects.filter(id_type_user__type_user_name='компания').order_by('-id')[:5][::-1]
        context['profileprog'] = Profile.objects.filter(id_type_user__type_user_name='программист').order_by('-id')[:5][::-1]
        context['vacancys'] = Vakancys.objects.all().order_by('-id')[:5][::1]
        context['countProfileCom'] = countProfileCom
        context['countProfileProg'] = countProfileProg
        context['countVacancys'] = countVacancys
        context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        return context