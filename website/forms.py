from django import forms


# from classroom.models import BookDemo
from crm.models import ContactUs, JoinUs
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'phone', 'email', 'message']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control','Placeholder':'Please enter your name'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'message': forms.Textarea(attrs={'class': 'form-control'}),
                   }


# class BookDemoForm(forms.ModelForm):
#     class Meta:
#         model = BookDemo
#         fields = ("__all__")
#         widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
#                    'phone': forms.NumberInput(attrs={'class': 'form-control'}),
#                    'age_group': forms.Select(attrs={'class': 'form-control'}),
#                    'date': forms.DateField(attrs={'type': 'date'}),
#                    'time_slot': forms.Select(attrs={'class': 'form-control'}),
                   
#                    }


# class BookDemoForm(forms.ModelForm):
#     class Meta:
#         model = BookDemo
#         fields = ['name', 'phone', 'age_group', 'date', 'time']
#         widgets = {'date':forms.DateInput(attrs={'type':'date'})}

# class JobApplicationForm(forms.ModelForm):
#     class Meta:
#         model = JoinUs
#         fields = ['name', 'email', 'phone', 'dob', 'address', 'city', 'state', 'education', 'working_exp', 'proj_url', 'hobbies', 'strength', 'weakness', 'skills', 'discussion_topic', 'describe_life', 'describe_yourself', 'non_judgmental', 'counselling', 'declaration' ]
#         labels = {'name':'Enter Name','working_exp':'Work Experience'}
        
#         widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
#                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
#                    'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#                    'dob':forms.DateInput(attrs={'type':'date'}),
#                    'qualification': forms.TextInput(attrs={'class': 'form-control'}),
#                    'address': forms.TextInput(attrs={'class': 'form-control'}),
#                    'city': forms.TextInput(attrs={'class': 'form-control'}),
#                    'state': forms.Select(attrs={'class': 'form-control'}),
#                    }                   