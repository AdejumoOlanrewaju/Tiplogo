from django.urls import path
from .import views
urlpatterns=[
    path('',views.index , name= 'index'),
    path('contact', views.contact, name='contact'),
    path('mail',views.mail,name= 'mail'),
    path('tiplogo-cbt',views.tiplogo_cbt,name='tiplogo-cbt'),
    path('tiplogo-fish',views.tiplogo_fish,name='tiplogo-fish'),
    path('tiplogo-ict',views.tiplogo_ict,name='tiplogo-ict'),
    path('tiplogo-led',views.tiplogo_led,name='tiplogo-led'),
    path('login',views.login,name='login'),
    path('tiplogo-logistics',views.tiplogo_logistics,name='tiplogo-logistics'),
    path('tiplogo-post',views.tiplogopostview.as_view(),name ='tiplogo-post'),
    path('post-list',views.postpageview.as_view(),name ='post-list'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name ='update'),
    path('delete<int:pk>/',views.DeletePostView.as_view(),name ='delete'),
]