from django.test import SimpleTestCase
from comments.forms import CommentForm

class TestForms(SimpleTestCase):
    def test_comment_forms_valid_data(self):
        
        form = CommentForm(data={
            'text':'hello world'
        })
        self.assertTrue(form.is_valid())
    
    def test_comment_forms_no_data(self):
        form = CommentForm(data = {})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)