from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.users.models import Profile
from app.msg.models import Msg
from app.msg.forms import MsgForm
from app.users.count import countVacancys, countProfileProg, countProfileCom


#Сообщения
def inbox(request):
    profile = request.user.profile
    messageRecipient = Msg.objects.filter(recipient=profile)
    messageSender = Msg.objects.filter(sender=profile)
    unreadCount = f'({messageRecipient.filter(is_read=False).count()})'
    context = {'messageRecipient': messageRecipient,
               'messageSender': messageSender,
               'countVacancys': countVacancys,
               'countProfileProg': countProfileProg,
               'countProfileCom': countProfileCom,
               'unreadCount': f'({Msg.objects.filter(recipient=profile, is_read=False).count()})'
               }
    return render(request, 'msg/inbox.html', context)

#Просмотр сообщения
def viewMessage(request, pk):
    profile = request.user.profile
    msg = Msg.objects.get(id=pk)
    if msg.is_read == False and msg.sender != request.user.profile:
        msg.is_read = True
        msg.save()
    context = {'msg': msg,
               'countVacancys': countVacancys,
               'countProfileProg': countProfileProg,
               'countProfileCom': countProfileCom,
               'unreadCount': f'({Msg.objects.filter(recipient=profile, is_read=False).count()})'
               }
    return render(request, 'msg/message.html', context)

#Создание сообщения
def createMessage(request, pk):
    profile = request.user.profile
    recipient = Profile.objects.get(id=pk)
    form = MsgForm()
    sender = request.user.profile
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = sender
            msg.recipient = recipient
            msg.save()
            return redirect('inbox')

    context = {'recipient': recipient,
               'form': form,
               'countVacancys': countVacancys,
               'countProfileProg': countProfileProg,
               'countProfileCom': countProfileCom,
               'unreadCount': f'({Msg.objects.filter(recipient=profile, is_read=False).count()})'
               }
    return render(request, 'msg/message_form.html', context)

# удаление пользователя
class DeleteMessage(DeleteView):
    model = Msg
    template_name = 'msg/message_delete.html'
    success_url = reverse_lazy('inbox')

    def get_context_data(self, **kwargs):
        context = super(DeleteMessage, self).get_context_data(**kwargs)
        context['countProfileCom'] = countProfileCom
        context['countProfileProg'] = countProfileProg
        context['countVacancys'] = countVacancys
        if User.is_authenticated:
            context['unreadCount'] = f'({Msg.objects.filter(recipient=self.request.user.id, is_read=False).count()})'
        else:
            context['unreadCount'] = ''
        return context