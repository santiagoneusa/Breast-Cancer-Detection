from django.urls import path
from . import views

app_name = 'ai_model'

urlpatterns = [
    path('', views.home, name='home'),
    path('ai-model/', views.ai_model, name='ai_model'),
]