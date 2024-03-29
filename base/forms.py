from django import forms
from .models import Subcribers , MailMessage ,EmailTemplate ,TiplogoPost,JambPost,FishPost,Contact
from ckeditor.fields import RichTextField

class SubcribersForm(forms.ModelForm):
    class Meta:
        model = Subcribers
        fields = ['email',]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'


class EmailTemplateForm(forms.ModelForm):
    class Meta:
        model =EmailTemplate
        fields = ['subject','message',]
       


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
  


class TiplogoPostForm(forms.ModelForm):
    images = forms.FileField()
    class Meta:
        model = TiplogoPost
        fields  = ['title','images','content']

class JambPostForm(forms.ModelForm):
    images = forms.FileField()
    class Meta:
        model = JambPost
        fields  = ['title','images','content']


class FishPostForm(forms.ModelForm):
    images = forms.FileField()
    class Meta:
        model = FishPost
        fields  = ['title','images','content']