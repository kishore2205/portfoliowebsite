from django.urls import path
from . import views





urlpatterns =[
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),
    path('skill/', views.skill, name='skill'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
]