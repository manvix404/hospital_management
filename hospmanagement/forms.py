from django import forms
from .models import appointment

class AppointmentForm(forms.ModelForm):
    # name=forms.CharField()
    # email=forms.EmailField()
    # phone=forms.CharField()
    # date=forms.DateField()
    # dept=forms.CharField()
    # doctor=forms.CharField()
    
    class Meta:
        model=appointment
        fields=['doctor','patient_name','date','specialization','patient_email','patient_phone']