from django.urls import path
from app.users.views import create_user, login_user, logout_user\
    , profile, ProfileListProg, ProfileListCom, Index, ProfileDetail\
    , userAccount, editAccount, DeleteAccount
from app.projects.views import ProjectDetail
from app.vacancys.views import VacancysDetail
from app.msg.views import createMessage


urlpatterns = [
    #главная страница
    path('', Index.as_view(), name='index'),
    #авторизация
    path('registration/', create_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #профиль-аккаунта
    path('profile/', profile, name='profile'),
    path('profile_user/', userAccount, name='profile_user'),
    path('editAccount/', editAccount, name='editAccount'),
    path('deleteAccount/<int:pk>', DeleteAccount.as_view(), name='deleteAccount'),
    path('profile_user/projects/<int:pk>', ProjectDetail.as_view(), name='project'),
    path('profile_user/vacancys/<int:pk>', VacancysDetail.as_view(), name='vacancy'),
    #профиль-программиста
    path('profile_list_prog/', ProfileListProg.as_view(), name='программист'),
    path('profile_list_prog/create-message/<int:pk>', createMessage, name="profile_list_prog_create-msg"),
    path('profile_list_prog/<int:pk>', ProfileDetail.as_view(), name='profile_detail_prog'),
    path('profile_list_prog/project/<int:pk>', ProjectDetail.as_view(), name='profile_detail_project'),
    #профиль-компании
    path('profile_list_com/', ProfileListCom.as_view(), name='компания'),
    path('profile_list_com/<int:pk>', ProfileDetail.as_view(), name='profile_detail_com'),
    path('profile_list_com/create-message/<int:pk>', createMessage, name="profile_list_com_create-msg"),
    path('profile_user/vacancys/company/<int:pk>', ProfileDetail.as_view(), name='profile_detail_com_vak'),
    path('profile_list_com/vacancys/<int:pk>', VacancysDetail.as_view(), name='profile_detail_vacancy'),
    path('profile_list_com/vacancys/company/<int:pk>', ProfileDetail.as_view(), name='pprofile_detail_vacancy_com_vak'),
    ]