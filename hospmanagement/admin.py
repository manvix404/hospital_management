from django.contrib import admin
from .models import Doctor, Vaccinations,report,appointment,bookvac

class AppointmentInLine(admin.TabularInline):
    model=appointment
    extra=0

class VaccineInLine(admin.TabularInline):
    model=bookvac
    extra=0

class VaccineAdmin(admin.ModelAdmin):
    inlines=[VaccineInLine]

class DoctorAdmin(admin.ModelAdmin):
    inlines=[AppointmentInLine]
# Register your models here.
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(report)
admin.site.register(Vaccinations,VaccineAdmin)
