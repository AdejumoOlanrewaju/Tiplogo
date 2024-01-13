from django_pandas.io import  read_frame 
from django.shortcuts import render ,redirect
from .forms import SubcribersForm ,MailMessageForm
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from .models import Subcribers ,MailMessage
from  django.core.mail import send_mail

 
# Create your views here.
def index(request):

    return render(request, 'index.html')

def news(request):
        if request.method == 'POST': 
            email =request.POST['email']
            if Subcribers.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
                return redirect ('news') 
            else:
                 sub = Subcribers.objects.create(email=email)
                 sub.save()
                 messages.success(request, 'email added succesfully')
                 return redirect ('news') 
        else: 
            form = SubcribersForm()
            context = {
                'form':form
            }
            return render (request, 'news.html', context)
        
def mail(request):
     emails=Subcribers.objects.all()
     db =read_frame(emails, fieldnames = ['email'])
     mail_letter = db['email'].values.tolist()
     print(mail_letter)
     if request.method == 'POST':
          form = MailMessageForm(request.POST)
          if form.is_valid():
               form.save()
               title = form.cleaned_data.get('title')
               message = form.cleaned_data.get('message')
               send_mail(
                    title,
                    message,
                    '',
                    mail_letter, 
                    fail_silently=False,
               )
               messages.success(request, 'mail sent successfully')
               return redirect ('mail')
     else:    
         form = MailMessageForm()
         context = {
              'form':form
         }
         return render (request, 'mail.html', context)

  



                    
         


       
 