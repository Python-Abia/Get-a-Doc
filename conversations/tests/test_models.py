from django.test import TestCase
from conversations.models import Conversation
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        
        self.user = self.setup_user()
        self.user.save()
        
        
        self.Conversation1 = Conversation.objects.create(
            sender_id =self.user,
            receiver_id =self.user,
            text    = 'hello world',
        )
        
     
    @staticmethod
    def setup_user():
        return User.objects.create_user(
            username ='uba',
            email = 'ucktech@gmail.com',
            password = '4567vn',
        )   
        
    def test_get_conversation(self):
        self.assertEquals(self.Conversation1.text, 'hello world')
