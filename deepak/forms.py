from django import forms
from .models import BloodRequest


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = [
            'full_name',
            'phone',
            'email',
            'blood_group',
            'units',
            'hospital',
            'needed_date',
            'message',
        ]
        labels = {
            'full_name': 'Patient or contact full name',
            'phone': 'Contact phone',
            'email': 'Email',
            'blood_group': 'Blood group needed',
            'units': 'Units needed',
            'hospital': 'Hospital or care center',
            'needed_date': 'Date needed',
            'message': 'Additional details (optional)',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter full name',
                'autocomplete': 'name',
            }),
            'phone': forms.TelInput(attrs={
                'placeholder': 'Enter phone number',
                'autocomplete': 'tel',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'name@example.com',
                'autocomplete': 'email',
            }),
            'blood_group': forms.Select(),
            'units': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'hospital': forms.TextInput(attrs={
                'placeholder': 'Enter hospital or care center',
            }),
            'needed_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Add any helpful details for the blood bank',
            }),
        }
