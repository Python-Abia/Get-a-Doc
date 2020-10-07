from django.test import TestCase
from conversations.models import Conversation


class TestModels(TestCase):
    def setUp(self):
        self.Conversation1 = Conversation.objects.create(
            user = "ucktech",
            text    = " hello world",
        )
 
    def test_get_conversation(self):
        self.assertEquals(self.Conversation1.text, 'hello world')
        