from django.test import SimpleTestCase
from conversations.forms import ConversationForms

class TestForms(SimpleTestCase):
    def test_conversation_forms_valid_data(self):
        
        form = ConversationForms(data={
            'text':'hello world'
        })
        self.assertTrue(form.is_valid())
    
    def test_conversation_forms_no_data(self):
        form = ConversationForms(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)