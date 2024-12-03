from django.urls import path, include
from .views import list_patients

urlpatterns = [
    path('', list_patients)
]
