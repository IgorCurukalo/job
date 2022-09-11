from django.urls import path
from app.users.views import create_user, login_user, logout_user\
    , profile, ProfileListProg, ProfileListCom, Index, ProfileDetail\
    , userAccount, editAccount, deleteAccount
from app.projects.views import ProjectDetail


urlpatterns = [
    path('', Index.as_view(), name='index'),
    #авторизация
    path('registration/', create_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #профили-акканты
    path('profile/', profile, name='profile'),
    path('profile_user/', userAccount, name='profile_user'),
    path('editAccount/', editAccount, name='editAccount'),
    path('deleteAccount/<int:pk>', deleteAccount.as_view(), name='deleteAccount'),
    path('profile_user/<int:pk>', ProjectDetail.as_view(), name='project'),
    #профили-программистов
    path('profile_list_prog/', ProfileListProg.as_view(), name='программист'),
    path('profile_list_prog/<int:pk>', ProfileDetail.as_view(), name='profile_detail'),
    path('profile_list_prog/project/<int:pk>', ProjectDetail.as_view(), name='profile_detail_project'),
    #профили-компании
    path('profile_list_com/', ProfileListCom.as_view(), name='компания'),
    path('profile_list_com/<int:pk>', ProfileDetail.as_view(), name='profile_detail'),
    ]