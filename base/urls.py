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
  # <<<<<<<-------------------------FISH CMS--------------------------->>>>>>
    path('fish-post',views.tiplogofishpost.as_view(),name ='fish-post'),
    path('update/<int:pk>/',views.fishpostupdateview.as_view(),name ='update'),
    path('delete<int:pk>/',views.DeleteFishPost.as_view(),name ='delete'),
     # <<<<<<<--------------------------JAMB CMS--------------------------->>>>>>
    path('jamb-post',views.tiplogojambpost.as_view(),name ='jamb-post'),
    path('update/<int:pk>/',views.jambpostupdateview.as_view(),name ='update'),
    path('delete<int:pk>/',views.DeleteJambPost.as_view(),name ='delete'),
    path('email-list',views.emalistviews.as_view(),name='email-list'),
]