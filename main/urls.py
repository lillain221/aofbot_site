from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('achievement/', views.achievement, name='achievement'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('skill/', views.skill, name='skill'),

]
