from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'password1',
            'password2',
        ]
        
        
    def __init__(self, *args, **kwargs):	    
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control', 'id':'firstname', 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control', 'id':'password', 'placeholder':'Last Name'})
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'id':'username', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'id':'email', 'placeholder':'Email'})
        self.fields['phone'].widget.attrs.update({'class' : 'form-control', 'id':'phone', 'placeholder':'Phone'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control', 'id':'password', 'placeholder':'password'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control', 'id':'password', 'placeholder':'confirm password'})
