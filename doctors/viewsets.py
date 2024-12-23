from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from .permissions import IsDoctor

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]

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