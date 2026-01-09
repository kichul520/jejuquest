from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
    path('pre-register/', views.pre_register, name='pre_register'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
