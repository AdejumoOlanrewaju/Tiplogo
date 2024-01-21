from django.contrib import admin
from  .models import Subcribers ,MailMessage ,EmailTemplate,JambPost,FishPost, TiplogoPost 
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from ckeditor.fields import RichTextField

# Register your models here.


class EmailTemplateFormAdminForm(forms.ModelForm):
    class Meta:
        model =EmailTemplate
        fields ='__all__'
        widgets ={
            'message':RichTextField(),

        }


class EmailTemplateAdmin(admin.ModelAdmin):
    form =EmailTemplateFormAdminForm

    def save_model(self ,request ,obj ,form ,change):
        super().save_model(request,obj,form,change)
        subject =obj.subject
        html_message =obj.message

        recipients =[subcriber.email for subcriber in obj.recipients.all()]
        from_email =settings.EMAIL_HOST_USER
        send_mail(
            subject ,'',from_email ,recipients ,fail_silently=False, html_message=html_message
        )


admin.site.register(Subcribers)
admin.site.register(MailMessage)
admin.site.register(TiplogoPost)
admin.site.register(JambPost)
admin.site.register(FishPost)
admin.site.register(EmailTemplate,EmailTemplateAdmin) 