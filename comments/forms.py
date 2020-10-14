from django.forms import ModelForm
from . models import Comment

class CommentForm(ModelForm):
    
    class Meta:
        model ="Comment"
        fields =[
            'text'
        ]
    
    def __init__(self, *args, **kwargs):	    
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'form-control', 'id':'text', 'placeholder':'text'})
