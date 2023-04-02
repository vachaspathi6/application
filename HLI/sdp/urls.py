from django.urls import path
from . import views
urlpatterns=[
    path('',views.function1),
    path('home/',views.function2,name='home'),
    path('about/',views.function3,name='about'),
    path('policies/',views.function4,name='policies'),
    path('claims/',views.function5,name='claims'),
    path('payment/',views.function6,name='payment'),
    path('service/',views.function7,name='service'),
    path('profile/',views.function8,name='profile'),
    path('date/',views.function9,name='datetime'),
    path('settings/',views.function10,name='settings'),
    path('help/', views.function11, name='help'),
    path('qrcode/', views.function12, name='qrcode'),
    path('contactus1/', views.contactus1, name='contactus1'),
    path('sign/', views.sign, name='sign'),
    path('login/', views.checkuserlogin, name='login'),
    path('table1/', views.function14, name='table1'),
    path('ALLSQLcommands.pdf/', views.function15, name='ALLSQLcommands.pdf'),
]