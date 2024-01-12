from django import forms
from .models import Subcribers , MailMessage

class SubcribersForm(forms.ModelForm):
    class Meta:
        model = Subcribers
        fields = ['email',]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'