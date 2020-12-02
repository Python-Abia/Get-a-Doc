from django import forms
from .models import Inquiry


class Inquiryform(forms.ModelForm):
    
    class Meta:
        model = Inquiry
        
        fields = [
               'title',
               'category',
               'user',
               'details',
        ]
    
    def __init__(self, *args, **kwargs):	    
        super(Inquiryform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'id':'first_name', 'placeholder':'title'})
        self.fields['category'].widget.attrs.update({'class' : 'form-control', 'id':'first_name', 'placeholder':'category'})
        self.fields['user'].widget.attrs.update({'class' : 'form-control', 'id':'username', 'placeholder':'user'})
        self.fields['details'].widget.attrs.update({'class' : 'form-control', 'id':'email', 'placeholder':'details'})
        