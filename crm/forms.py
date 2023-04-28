from django import forms
from django.forms import fields, models
from .models import ContactUs, ContactLeadFollowUp




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['query_status','name', 'phone', 'email', 'message']        
        widgets = {
            'query_status': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
                   }


class AddContactFollowupForm(forms.ModelForm):
    class Meta:
        model = ContactLeadFollowUp
        fields = [ 'contact', 'note', 'next_followup_date', 'next_followup_time', 'owner']
        widgets = {
            'contact': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
            'next_followup_date':forms.DateInput(attrs={'type':'date','class': 'form-control' }),
            'next_followup_time':forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            
            }