from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    fields = '__all__'


admin.site.register(Patient)

