from django import forms
from django.forms import ModelForm
from app.msg.models import Msg


#форма сообщений
class MsgForm(ModelForm):
    class Meta:
        model = Msg
        fields = ['sender', 'recipient', 'name_msg', 'body']
        widgets = {
            'body': forms.Textarea(),
        }