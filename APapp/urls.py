from django.contrib import admin
from django.urls import path
from APapp import views
urlpatterns = [
 path("", views.index, name='index'),
 path('register', views.register, name='register'),
 path('message', views.message, name='message'),
 path('Account',views.Account, name='Account'),
 path('Message',views.Message, name='Message'),
 path('speakers', views.speakers, name='speakers'),
 path('partners', views.partners, name='partners'),
 path('compitition', views.compitition, name='compitition'),
 path('incentive', views.incentive, name='incentive'),
 path('sector', views.sector, name='sector'),




]