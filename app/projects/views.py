from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.projects.models import Project
from app.users.count import countVacancys, countProfileProg, countProfileCom
from app.msg.models import Msg

# создание проекта
class AddProject(CreateView):
    model = Project
    template_name = 'projects/project_add.html'
    fields = ['title', 'image', 'description', 'demo_link']
    success_url = reverse_lazy('profile_user')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProject, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddProject, self).get_context_data(**kwargs)
        context['countProfileCom'] = countProfileCom
        context['countProfileProg'] = countProfileProg
        context['countVacancys'] = countVacancys
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


# изменение проекта
class EditProject(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    fields = ['title', 'image', 'description', 'demo_link']
    success_url = reverse_lazy('profile_user')

    def get_context_data(self, **kwargs):
        context = super(EditProject, self).get_context_data(**kwargs)
        context['countProfileCom'] = countProfileCom
        context['countProfileProg'] = countProfileProg
        context['countVacancys'] = countVacancys
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context

# удаление проекта
class DeleteProject(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('profile_user')

    def get_context_data(self, **kwargs):
        context = super(DeleteProject, self).get_context_data(**kwargs)
        context['countProfileCom'] = countProfileCom
        context['countProfileProg'] = countProfileProg
        context['countVacancys'] = countVacancys
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context


# детализация проекта
class ProjectDetail(DetailView):
    model = Project
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        context['countProfileCom'] = countProfileCom
        context['countProfileProg'] = countProfileProg
        context['countVacancys'] = countVacancys
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context

