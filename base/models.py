from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Subcribers(models.Model):
    email = models.EmailField(unique=True)
    date =models.DateTimeField(db_default = datetime.now())

    def __str__(self):
        return self.email
    

class  MailMessage(models.Model):
    title = models.CharField(max_length= 123)
    message = models.TextField()
    def __str__(self):
        return self.title
    
class EmailTemplate(models.Model):
    subject = models.CharField(max_length=123)
    message =RichTextField()
   
    
    def __str__(self):
        return self.subject
    
class TiplogoPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(db_default = datetime.now())

    def __str__(self):
        return self.title
    
class JambPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(db_default = datetime.now())

    def __str__(self):
        return self.title
    
class FishPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    images = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(db_default = datetime.now())

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name 

