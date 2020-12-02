from django import forms
from . models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model ="Comment"
        fields ='__all__'
    
    # django bootstrap form
    def __init__(self, *args, **kwargs):	    
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'form-control', 'id':'text', 'placeholder':'text'})
