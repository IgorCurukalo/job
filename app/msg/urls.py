from django.urls import path
from app.msg.views import inbox, viewMessage, createMessage


urlpatterns = [
    #сообщения
    path('inbox/', inbox, name="inbox"),
    path('message/<int:pk>', viewMessage, name="msg"),
    path('create-message/<int:pk>', createMessage, name="create-msg"),
    ]