from django.shortcuts import render
from .serializers import PatientSerializer, Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
# Create your views here.
# GET /api/patients => Listar
# POST /api/patients => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients/<pk> => Modificación
# DELETE /api/patients/<pk> => Borrar



@api_view(("GET","POST"))
def list_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients,many=True)

        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def detail_patient(request,pk):
    patient = get_object_or_404(Patient,id=pk)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PatientSerializer(patient,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        updated = {
            "message": "Patient updated successfully",
            "data": serializer.data
        }

        return Response(updated,status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


# ejemplo
@api_view(["POST"])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)  # Deserializar los datos enviados por el cliente
    if serializer.is_valid():  # Verificar si los datos son válidos
        serializer.save()  # Guardar el nuevo paciente en la base de datos
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Devolver los datos del paciente creado
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si hay errores, devolverlos