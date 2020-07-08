from django import forms
from .models import Enquiry, Pull


class ModalEnquiry(forms.ModelForm):
    class Meta:
        model = Enquiry

        fields = {
            'customer_name',
            'number',
            'email',
            'question',

        }

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Customer name'

            }),

            'number': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Customer number'

            }),

            'email': forms.EmailInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Email'

            }),

            'question': forms.Textarea(attrs={
                'content': 'Textarea',
                'class': "form-control inp",
                'placeholder': 'Enquiry'

            }),
        }


class PulllEnquiry(forms.ModelForm):
    class Meta:
        model = Pull

        fields = {
            'number'
        }

        widgets = {
            'number': forms.TextInput(attrs={
                'class': "form-control inp",
                'placeholder': 'Enquiry ID'

            }),

        }
