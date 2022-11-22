from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.vacancys.models import Vakancys
from app.vacancys.forms import VakancysUpdateForm, VakancysAddForm
from app.vacancys.filters import VacancysFilter
from app.users.models import Profile
from app.msg.models import Msg


# создание вакансии
class AddVacancy(CreateView):
    model = Vakancys
    form_class = VakancysAddForm
    template_name = 'vacancys/vacancy_add.html'
    success_url = reverse_lazy('profile_user')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(AddVacancy, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddVacancy, self).get_context_data(**kwargs)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context

# изменение вакансии
class EditVacancy(UpdateView):
    model = Vakancys
    form_class = VakancysUpdateForm
    template_name = 'vacancys/vacancy_update.html'
    success_url = reverse_lazy('profile_user')

    def get_context_data(self, **kwargs):
        context = super(EditVacancy, self).get_context_data(**kwargs)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


# удаление вакансии
class DeleteVacancy(DeleteView):
    model = Vakancys
    template_name = 'vacancys/vacancy_delete.html'
    success_url = reverse_lazy('profile_user')

    def get_context_data(self, **kwargs):
        context = super(DeleteVacancy, self).get_context_data(**kwargs)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


# детализация вакансии
class VacancysDetail(DetailView):
    model = Vakancys
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(VacancysDetail, self).get_context_data(**kwargs)
        context['vacancys'] = Vakancys.objects.filter(id=self.object.id)
        context['profile'] = Profile.objects.filter(profile_name=self.object.profile.profile_name)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''

        #добавляет количество просмотра + 1
        v = Vakancys.objects.filter(id=self.object.id)
        for i in v:
            i.count = str(int(i.count) + 1)
            i.save()
        return context


#Список вакансий
class VacancysList(FilterView):
    model = Vakancys
    filterset_class = VacancysFilter
    context_object_name = 'vacancys'
    template_name = 'vacancys/vacancys_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(VacancysList, self).get_context_data(**kwargs)
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context

def VakCount(request):

    if(Vakancys.objects.count() <= 0):
        x = Vakancys.objects.create()
        x.save()
    else:
        x = Vakancys.objects.all()[0]
        x.count = x.count + 1
        x.save()
    context = {'count': x.count}
    return render(request, 'vacancys/vacancys_detail.html', context=context)