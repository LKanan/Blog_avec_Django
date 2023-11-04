from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_accueil_view, name='page_accueil'),
]
