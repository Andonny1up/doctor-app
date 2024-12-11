from django.urls import path, include
from .views import ListPatientView, DetailPatientView

urlpatterns = [
    path('', ListPatientView.as_view()),
    path('<int:pk>/', DetailPatientView.as_view())
]
