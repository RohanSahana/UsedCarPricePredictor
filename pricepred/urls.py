from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Predictor, name='fp'),
    path('', views.Predictor, name = 'Predictor'),
    path('result/', views.result, name='result'),
]