from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from patients.models import Patient
from .models import Doctor

# Create your tests here.
class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Luis',
            last_name='Magordito',
            date_of_birth='1990-12-05',
            contact_number='2121312313',
            email='patient@example.com',
            address='Dirección de prueba',
            medical_history='Ninguna'
        )

        self.doctor = Doctor.objects.create(
            first_name = 'Oscar',
            last_name = 'Caracas',
            qualification = 'Profesional',
            contact_number = '1651516516',
            email = 'doctor@example.com',
            address = 'Nose',
            biography = 'Si',
            is_on_vacation = False 
        )

        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse('doctor-appointments',kwargs={"pk":self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)