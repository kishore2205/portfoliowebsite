from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'user_name',
            'user_email',
            'user_phone',
            'category',
            'dob',
            'age',
            'gender',
            'message'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'readonly': True}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
