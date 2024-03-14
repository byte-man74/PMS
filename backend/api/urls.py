from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
     path('api/patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('api/patients/<int:pk>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-retrieve-update-destroy'),
]
