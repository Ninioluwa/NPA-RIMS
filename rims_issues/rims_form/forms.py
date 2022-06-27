from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from .models import IssuesModel

User = get_user_model()


class RimsForm(forms.Form):
    CHOICES = [
        ('NEW', 'New'),
        ('RESOLVED', 'Resolved')
     ]

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border-2'}))
    status = forms.ChoiceField(choices=CHOICES, 
        widget=forms.Select(attrs={'class': 'border-2'}))
    sen_no = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border-2'}))
    issues = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'border-2'}))


class RimsModelForm(forms.ModelForm):
    CHOICES = [
            ('NEW', 'New'),
            ('RESOLVED', 'Resolved')
        ]

    subject = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "text-gray-800 block w-full px-3 py-2 mb-3 text-sm leading-tight  border rounded ",
                    "readonly": True,
                    }))
    status = forms.ChoiceField(choices=CHOICES, 
            widget=forms.Select(
                attrs={
                    "class":"text-gray-800 block mb-3 px-3 py-2 w-full text-sm leading-tight  border rounded",
                    }))
    sen_no = forms.CharField(
            widget=forms.TextInput(attrs={
                "class": "text-gray-800 block w-full px-3 py-2 mb-3 text-sm leading-tight  border rounded ",
                "readonly": True,
                }))
    issues = forms.CharField(
            widget=forms.Textarea(attrs={
                "class": "text-gray-800 block w-full px-3 py-2 mb-3 text-sm leading-tight  border rounded ",
                "readonly": True,
                }))

    class Meta:
        model = IssuesModel
        fields = {
            'subject',
            'sen_no',
            'status',
            'issues',
            
        }


class CustomUserCreationForm(UserCreationForm):
    CHOICES = [
        ('----', '----------'),
        ('LAGOS', 'Lagos'),
        ('TIN-CAN', 'Tin-Can'),
        ('RIVERS', 'Rivers'),
        ('DELTA', 'Delta'),
        ('CALABAR', 'Calabar'),
        ('ONNE', 'Onne')
    ]

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
        "class": "text-gray-800 block w-full px-3 py-2 mb-3 text-sm leading-tight  border rounded ",
        "size":"50",
        "placeholder":"Email" 
        }))
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "text-gray-800 block w-full px-3 py-2 mb-3 text-sm leading-tight  border rounded ",
        "size":"50",
        "placeholder":"Name"
        }))

    port = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={
        "class":"text-gray-800 block mb-3 px-3 py-2 w-full text-sm leading-tight  border rounded",
        
        
    }))
                    
    class Meta:
        model = User
        fields = ("username", "email", "port", "password1", "password2")
        field_classes = {'username': UsernameField}
        
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class']="block mb-3 px-3 py-2 w-full text-sm leading-tight text-gray-800  border rounded"
        self.fields['password1'].help_text=None
        self.fields['password2'].widget.attrs['class']="block mb-3 px-3 py-2 w-full text-sm leading-tight text-gray-800  border rounded"
        self.fields['password2'].help_text=None



class AuthorizeUserForm(forms.Form):
    is_active=forms.BooleanField(
        widget=forms.CheckboxInput, label=User)