from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.template import Context, loader
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from django.conf import settings
from django.http import HttpResponseRedirect
from app.users.forms import RegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm, ProfileUpdateFormAvatar
from app.users.models import Profile
from app.users.filters import ProfileFilter

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
        'form': form
    }
    return render(request, 'users/registration.html', context=context)

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
        'form': form
    }
    return render(request, 'users/login.html', context=context)

def logout_user(request):

    auth.logout(request)
    return redirect('index')

@login_required
def profile(request):
    user = request.user
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
        'p_form_avatar': p_form_avatar
    }
    return render(request, 'users/profile.html', context)

@login_required
def userAccount(request):
    profile = request.user.profile
    skills = profile.skills.all()
    context = {'profile': profile, 'skills': skills}
    return render(request, 'users/profile_account.html', context)

@login_required
def editAccount(request):
    user = request.user
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
        if request.user.profile.image != 'profile_images/default.jpg':
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            p_form_avatar = ProfileUpdateFormAvatar(instance=request.user.profile)
        else:
            return redirect('index')
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'p_form_avatar': p_form_avatar
    }
    return render(request, 'users/profile.html', context)


class ProfileListCom(FilterView):

    model = Profile
    filterset_class = ProfileFilter
    context_object_name = 'profile'
    template_name = 'users/profile_list.html'
    queryset = Profile.objects.filter(id_type_user__type_user_name='компания')
    paginate_by = 3


class ProfileListProg(FilterView):

    model = Profile
    filterset_class = ProfileFilter
    context_object_name = 'profile'
    template_name = 'users/profile_list.html'
    queryset = Profile.objects.filter(id_type_user__type_user_name='программист')
    paginate_by = 3


class ProfileDetail(DetailView):

    model = Profile
    pk_url_kwarg = 'pk'


class Index(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.queryset
        return context