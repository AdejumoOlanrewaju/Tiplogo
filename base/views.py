
from typing import Any
from django.core.mail import EmailMessage
from django.shortcuts import render ,redirect ,get_object_or_404
from .forms import SubcribersForm ,MailMessageForm ,ContactForm, EmailTemplateForm,TiplogoPostForm,FishPostForm,JambPostForm
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from .models import Subcribers ,MailMessage ,EmailTemplate, TiplogoPost ,FishPost,JambPost
from  django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.management.base import BaseCommand
from django.contrib.auth import authenticate
from django.views import generic
from django.contrib import auth

 
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
            recipients_list =list(subcriber_list)
            print(subcriber_list)
            
            email =EmailMessage(
                subject,
                message,
                from_email,
            recipients_list
                
            )
            email.send()
            messages.success(request, f'email sent successfully  to{subcriber_list}')
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



       
def tiplogo_cbt(request):
    return render (request, 'tiplogo_cbt.html')

def tiplogo_fish(request):
    return render (request, 'tiplogo_fish.html')

def tiplogo_ict(request):
    return render (request, 'tiplogo_ict.html')

def tiplogo_led(request):
    return render (request, 'tiplogo_led.html')

def tiplogo_logistics(request):
    return render (request, 'tiplogo_logistics.html')

def login(request):
    if request.method =='POST':
        username =request.POST['username']
        password =request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('tiplogo-post')
        else:
            messages.error(request, 'username and password do not match')
            return redirect ('login')
    else:
        return render ( request, 'TIPLOGO CMS/login.html')
    
# TIPLOGO CONTENT MANAGEMENT SYSTEM
    
 # <<<<<<<--------------------------LED CMS POST ------------------------------------->>>>>>
    
class tiplogopostview(generic.CreateView):
    template_name = 'TIPLOGO CMS/LED/tiplogo_post.html'
    form_class = TiplogoPostForm
    def get_success_url(self):
        return reverse('post-list')
    
class postpageview(generic.ListView):
    template_name = 'TIPLOGO CMS/post_list.html'
    queryset = TiplogoPost.objects.all()
    context_object_name = 'post_list'
    def post_list(request):
        post_list = TiplogoPost.objects.all()
        context = {
            'post_list':post_list
        }
        return render (request , 'TIPLOGO CMS/post_list.html',context)
    
class PostUpdateView(generic.UpdateView):
    model = TiplogoPost
    form_class = TiplogoPostForm
    template_name = 'TIPLOGO CMS/update.html'
    def get_success_url(self):
        return reverse('post-list')
    def update(request ,pk):
        if request.method == 'POST':
            instance = get_object_or_404(TiplogoPost ,pk=pk)
            form = TiplogoPostForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('post-list')
        else:
            form = TiplogoPostForm(instance=instance)
            context = {
                'form':form
            }
            return render(request, 'update.html',context)
    
class DeletePostView(generic.DeleteView):
    model = TiplogoPost
    template_name = 'TIPLOGO CMS/delete.html'
    def get_success_url(self):
        return reverse('post-list')
    
     # <<<<<<<--------------------------FISH CMS POST ------------------------------------->>>>>>

class tiplogofishpost(generic.CreateView):
    template_name = 'TIPLOGO CMS/FISH/fish_post.html'
    model = FishPost
    form_class = FishPostForm
    def get_success_url(self):
        return reverse ('post-list')
    

class fishpostupdateview(generic.UpdateView):
    template_name = 'TIPLOGO CMS/FISH/update.html'
    form_class = FishPostForm
    model =  FishPost
    def get_success_url(self):
        return reverse('post-list')
    def  updatefish(request , pk):
        instance = get_object_or_404 (FishPost ,pk=pk)
        if request.method == 'POST':
            form = FishPostForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect ('post-list')
        else:
            form = FishPostForm(instance=instance)
            context= {
                'form':form
            }
            return render (request, 'update.html',context)
            
        
class DeleteFishPost(generic.DeleteView):
    model = FishPost
    template_name = 'TIPLOGO CMS/FISH/delete.html'
    def get_success_url(self):
        return reverse('post-list')
    
    # <<<<<<<--------------------------JANB CMS POST ------------------------------------->>>>>>

class tiplogojambpost(generic.CreateView):
    template_name = 'TIPLOGO CMS/JAMB/jamb_post.html'
    model = JambPost
    form_class =JambPostForm
    def get_success_url(self):
        return reverse ('post-list')
    
class jambpostupdateview(generic.UpdateView):
    template_name = 'TIPLOGO CMS/JAMB/update.html'
    form_class = JambPostForm
    model =  JambPost
    def get_success_url(self):
        return reverse('post-list')
    def  updatefish(request , pk):
        instance = get_object_or_404 (JambPost ,pk=pk)
        if request.method == 'POST':
            form = JambPostForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect ('post-list')
        else:
            form = JambPostForm(instance=instance)
            context= {
                'form':form
            }
            return render (request, 'update.html',context)


class DeleteJambPost(generic.DeleteView):
    model = JambPost
    template_name = 'TIPLOGO CMS/JAMB/delete.html'
    def get_success_url(self):
        return reverse('post-list')
     # <<<<<<<-------------------------- THE END OF CMS------------------------------------->>>>>>
    
class emalistviews(generic.ListView):
    template_name = 'TIPLOGO CMS/email_list.html'
    queryset = Subcribers.objects.all()
    model =Subcribers
    context_object_name = 'emails'
    def email(request):
        emails = Subcribers.objects.all()
        context = {
            'emails':emails
        }
        return render (request, 'TIPLOGO CMS/email_list.html',context)
