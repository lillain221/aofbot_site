from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('achievement/', views.achievement, name='achievement'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('google2243e3042b43a5c5.html/', views.google2243e3042b43a5c5, name='google2243e3042b43a5c5'),
    path('simulator', views.simulator_page, name='simulator_page'),
    path('result', views.result, name='result'),
]
