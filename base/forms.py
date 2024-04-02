from django import forms
from .models import Subcribers , MailMessage ,EmailTemplate ,TiplogoPost,JambPost,FishPost
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
       


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)


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