from django.urls import path
from app.msg.views import inbox, viewMessage, createMessage, DeleteMessage


urlpatterns = [
    #сообщения
    path('inbox/', inbox, name="inbox"),
    path('message/<int:pk>', viewMessage, name="msg"),
    path('create-message/<int:pk>', createMessage, name="create-msg"),
    path('message/<int:pk>/delete', DeleteMessage.as_view(), name="delete-msg"),
    ]