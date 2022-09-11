from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.projects.models import Project


# создание проекта
class AddProject(CreateView):
    model = Project
    template_name = 'projects/project_add.html'
    fields = ['title', 'image', 'description', 'demo_link']
    success_url = reverse_lazy('profile_user')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProject, self).form_valid(form)


# изменение проекта
class EditProject(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    fields = ['title', 'image', 'description', 'demo_link']
    success_url = reverse_lazy('profile_user')


# удаление проекта
class DeleteProject(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('profile_user')


# детализация проекта
class ProjectDetail(DetailView):
    model = Project
    pk_url_kwarg = 'pk'


    # def get_context_data(self, **kwargs):
    #     context = super(ProfileDetail, self).get_context_data(**kwargs)
    #     context['vacancis'] = Vacanci.objects.filter(user=self.object.user)
    #     return context


