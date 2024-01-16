
from typing import Any
from django.core.mail import EmailMessage
from django.shortcuts import render ,redirect
from .forms import SubcribersForm ,MailMessageForm ,ContactForm, EmailTemplateForm
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from .models import Subcribers ,MailMessage ,EmailTemplate
from  django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.management.base import BaseCommand

 
# Create your views here.
def index(request):

    return render(request, 'index.html')

def news(request):
    email =Subcribers.email
    if request.method == 'POST':
     form =SubcribersForm(request.POST)
     if form.is_valid():
         subcriber=form.save()
         send_thanks_mail(subcriber.email)
         messages.success(request, 'email added successfully')
         return redirect('news')
     else:
         Subcribers.objects.filter(email=email).exists()
         messages.error(request, 'email already exist')
         return redirect('news')
    else:
     form =SubcribersForm()
     context ={
         'form':form
     }
     return render (request,'news.html',context)
def send_thanks_mail(email):
    subject = 'thank you for subcribing'
    html_message =render_to_string('thank_you.html')
    plain_message= strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=html_message,
        fail_silently=True
    )
    
       
        
def mail(request):
    if request.method == 'POST':
        form = EmailTemplateForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message =form.cleaned_data['message']
            from_email =settings.DEFAULT_FROM_EMAIL
            subcriber_list =Subcribers.objects.values_list('email',flat=True)
            print(subcriber_list)
            for subcriber_list in subcriber_list:
                        email =EmailMessage(
                            subject,
                            message,
                            from_email,
                            [subcriber_list],
                            
                        )
                        email.send()
                        messages.success(request, f'email sent successfully  to {subcriber_list}')
                        return redirect ('mail')
    else:
            form = EmailTemplateForm()
            context ={
                'form':form
            }
            
            return render (request ,'mail.html' ,context)
    
# class Command(BaseCommand):
#     help = 'send email in all subcriber in the database'
#     def handle(self, *args, **options):
#         email_content = EmailTemplate.objects.first()
#         if email_content:
#             subject =email_content.subject
#             message =email_content.message
#             from_email= settings.DEFAULT_FROM_EMAIL
#             subcriber_list =Subcribers.objects.values_list('email',flat=True)
#             for subcriber_list in subcriber_list:
#                 try:
#                     email =EmailMessage(
#                         subject,
#                         message,
#                         from_email,
#                         [subcriber_list]
#                     )
#                     email.send()
#                     self.stdout.write(self.style.SUCCESS(f'successfully sent email to {subcriber_list}'))
#                 except Exception as e:
#                     self.stdout.write(self.style.ERROR(f'error sending mail to {subcriber_list}'))
#         else:
#             self.stdout.write(self.style.ERROR(f'no email found in the database.'),)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients_list =email
            # Send email
            send_mail(
                name,
                message,
                 recipients_list,
                ['vacan400@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)



       
 