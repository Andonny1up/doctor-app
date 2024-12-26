from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from bookings.serializers import AppointmentSerializer

class DoctorSerializer(serializers.ModelSerializer):

    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'qualification',
            'contact_number',
            'email',
            'address',
            'biography',
            'is_on_vacation',
            'appointments'
        ]

    def validate_email(self,value):
        #validar correos con @example.com

        if "@example.com" in value:
            return value
        
        raise serializers.ValidationError("El email debe incluir @example.com")


    def validate(self, attrs):

        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation']:
            raise serializers.ValidationError("Por favor, ingresa un numero valido antes de salir de vaciones")
        return super().validate(attrs)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'