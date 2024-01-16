from django.urls import path
from .import views
urlpatterns=[
    path('',views.index , name= 'index'),
    path('news',views.news, name= 'news'),
    path('contact', views.contact, name='contact'),
    path('mail',views.mail,name= 'mail'),
]