from django.test import TestCase
from comments.models import Comment
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self):
        
        self.user = self.setup_user()
        self.user.save()
    
        self.Comment1 = Comment.objects.create(
            sender_id =self.user,
            text    = 'hello world',
        )
    
    @staticmethod
    def setup_user():
        return User.objects.create_user(
            username ='uba',
            email = 'ucktech@gmail.com',
            password = '4567vn',
        )   
        
    def test_get_comment(self):
        self.assertEquals(self.Comment1.text, 'hello world')
