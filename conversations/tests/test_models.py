from django.test import TestCase
from conversations.models import Conversation


class TestModels(TestCase):
    def setUp(self):
        self.Conversation1 = Conversation.objects.create(
            first_name = "ucktech",
            last_name  = "ucktech",
            subject    = "test message",
            email      = "ucktech1@gmail.com",
            text    = " hello world",
        )
 
    def test_get_conversation(self):
        self.assertEquals(self.Conversation1.email, 'ucktech1@gmail.com')
        