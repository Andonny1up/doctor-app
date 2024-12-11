from django.urls import path, include
from .views import list_patients, detail_patient

urlpatterns = [
    path('', list_patients),
    path('/<int:pk>/', detail_patient)
]
