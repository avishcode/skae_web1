from django import forms
from django.forms import widgets
from classroom.models import *


class BookDemoForm(forms.ModelForm):
    class Meta:
        model = BookDemo
        fields = ['name', 'phone', 'age_group', 'date', 'time']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'age_group': forms.Select(attrs={'class': 'form-control'}),
                   'date':forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
                   'time': forms.Select(attrs={'class': 'form-control',}),
                   
                   }

class CreateClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        fields = ['class_type', 'class_room_name', 'start_time', 'end_time', 'no_of_rooms' ]
        widgets = {
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'class_room_name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time':forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}),
            'end_time':forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}),
            'no_of_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            }

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['classroom', 'room_status', 'room_name', 'days', 'trainer']            
        widgets = {
            'classroom': forms.Select(attrs={'class': 'form-control'}),
            'room_status': forms.Select(attrs={'class': 'form-control'}),
            'room_name': forms.TextInput(attrs={'class': 'form-control'}),
            'days': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            
        }

class CreateTimeSlot(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time', 'note', 'is_active']        
        widgets = {
            'start_time':forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}),
            'end_time':forms.TimeInput(attrs={'type':'time', 'class': 'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.CheckboxInput
        }

class UpdateTimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time', 'note', 'is_active']
        widgets = {
            'start_time':forms.TimeInput(attrs={'class':'form-control'}),
            'end_time':forms.TimeInput(attrs={'class':'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.CheckboxInput
        }
class CreateAgeGroupForm(forms.ModelForm):
    class Meta:
        model = AgeGroup
        fields = ['age_group', 'note']
        widgets = {
            'age_group': forms.TextInput(attrs={'class': 'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),
        }


class UpdateAgeGroupForm(forms.ModelForm):
    class Meta:
        model = AgeGroup
        fields = ['age_group', 'note', 'is_active'] 
        widgets = {
            'age_group':forms.TextInput(attrs={'class':'form-control'}),
            'note':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-control'}),
        }       