from django.urls import path
from app.vacancys.views import EditVacancy, DeleteVacancy, AddVacancy, VacancysList, VacancysDetail
from app.users.views import ProfileDetail

urlpatterns = [
    #вакансии
    path('vacancys/new/', AddVacancy.as_view(), name='addVacancy'),
    path('vacancys/<int:pk>/edit/', EditVacancy.as_view(), name='editVacancy'),
    path('vacancys/<int:pk>/delete/', DeleteVacancy.as_view(), name='deleteVacancy'),

    path('vacancys_list/', VacancysList.as_view(), name='findVacancy'),
    path('vacancys_list/<int:pk>', VacancysDetail.as_view(), name='detail_findVacancy'),
    path('vacancys_list/company/<int:pk>', ProfileDetail.as_view(), name='detail_findVacancy_com'),
    ]