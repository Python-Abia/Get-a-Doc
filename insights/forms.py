from django import forms
from .models import Insight

class Insightform(forms.ModelForm):
    
    class Meta:
        model = Insight
        
        fields = [
               'title',
               'slug',
               'body',
               'postImage',
        ]
    
    def __init__(self, *args, **kwargs):	    
        super(Insightform, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'id':'title', 'placeholder':'title'})
        self.fields['slug'].widget.attrs.update({'class' : 'form-control', 'id':'slug', 'placeholder':'slug'})
        self.fields['body'].widget.attrs.update({'class' : 'form-control', 'id':'body', 'placeholder':'body'})
        self.fields['postImage'].widget.attrs.update({'class' : 'form-control', 'id':'email', 'placeholder':'image'})
