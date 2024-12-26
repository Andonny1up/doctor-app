from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from .permissions import IsDoctor

from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(["POST"], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation =  True
        doctor.save()

        return Response({"status": "vacaciones activada"})
    

    @action(["POST"], detail=True)
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation =  False
        doctor.save()

        return Response({"status": "vacaciones desactivada"})
    

    @action(["POST","GET"], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self,request,pk):
        doctor = self.get_object()
        
        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments,many=True)
            return Response(serializer.data)