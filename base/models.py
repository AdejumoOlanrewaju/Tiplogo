from django.db import models
from datetime import datetime


class Subcribers(models.Model):
    email = models.EmailField()
    date =models.DateTimeField(db_default = datetime.now())

    def __str__(self):
        return self.email
    

class  MailMessage(models.Model):
    title = models.CharField(max_length= 123)
    message = models.TextField()
    def __str__(self):
        return self.title
    