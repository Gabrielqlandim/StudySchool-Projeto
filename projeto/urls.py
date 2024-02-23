from django.urls import path
from app.views import funcao

urlpatterns = [
    path('', funcao),
]
