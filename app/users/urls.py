from django.urls import path
from app.users.views import create_user, login_user, logout_user\
    , profile, ProfileListProg, ProfileListCom, Index, ProfileDetail\
    , userAccount, editAccount, ProjectDetail


urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('registration/', create_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('profile/', profile, name='profile'),
    path('editAccount/', editAccount, name='editAccount'),
    path('profile_user/', userAccount, name='profile_user'),
    path('profile_user/<int:pk>', ProjectDetail.as_view(), name='project'),

    path('profile_list_prog/', ProfileListProg.as_view(), name='программист'),
    path('profile_list_prog/<int:pk>', ProfileDetail.as_view(), name='profile_detail'),
    path('profile_list_prog/project/<int:pk>', ProjectDetail.as_view(), name='profile_detail_project'),

    path('profile_list_com/', ProfileListCom.as_view(), name='компания'),
    path('profile_list_com/<int:pk>', ProfileDetail.as_view(), name='profile_detail'),
    ]