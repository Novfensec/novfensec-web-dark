from django.urls import path, re_path
from . import views

urlpatterns=[
    path('', views.surface,name='home'),
    re_path(r'^about/?', views.about,name='about'),
    re_path(r'^portfolio/?', views.portfolio,name='portfolio'),
    re_path('contact/', views.contact,name='contact'),
    re_path(r'^signup/?', views.handlrSignUp,name='signup'),
    re_path(r'^login/?', views.handlrLogin,name='login'),
    re_path(r'^logout/?', views.handlrLogout,name='logout'),
    re_path(r'^codepen/?', views.codepen,name="codepen"),
    re_path(r'^github/?', views.github,name="github"),
    re_path(r'^channel/?', views.channel,name="channel"),
    re_path(r'^stackoverflow/?', views.stackoverflow,name="stackoverflow"),
]