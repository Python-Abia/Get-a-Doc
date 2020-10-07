from django.forms import ModelForm
from .models import Conversation

class ConversationForms(ModelForm):
    class Meta:
        model = Conversation
        fields = [
            'text'          
        ]
    
    
    def __init__(self, *args, **kwargs):	    
        super(ConversationForms, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'form-control', 'id':'text', 'placeholder':'text'})
