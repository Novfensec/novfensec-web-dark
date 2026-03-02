from django.urls import path
from . import views

urlpatterns=[
    path('', views.surface,name='home'),
    path('about/', views.about,name='about'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('contact/', views.contact,name='contact'),
    path('signup', views.handlrSignUp,name='signup'),
    path('login', views.handlrLogin,name='login'),
    path('logout/', views.handlrLogout,name='logout'),
    path('codepen/', views.codepen,name="codepen"),
    path('github/', views.github,name="github"),
    path('channel/', views.channel,name="channel"),
    path('stackoverflow/', views.stackoverflow,name="stackoverflow"),
]