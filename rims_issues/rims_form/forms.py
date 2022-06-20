
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import IssuesModel

User = get_user_model()

class RimsForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput (attrs={'class': 'border-2'}))
    status = forms.CharField(widget=forms.TextInput (attrs={'class': 'border-2'}))
    sen_no = forms.CharField(widget=forms.TextInput (attrs={'class': 'border-2'}))
    issues = forms.CharField(widget=forms.Textarea (attrs={'class': 'border-2'}))

class RimsModelForm(forms.ModelForm):
    class Meta:
        model = IssuesModel
        fields = {
            'subject',
            'sen_no',
            'status',
            'issues',
        }
 

 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User

        fields = ("username", "email" )
        field_classes = {'username': UsernameField}