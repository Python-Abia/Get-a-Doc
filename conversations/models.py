from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.git
class Conversation(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", default="")
    text = models.TextField(blank=False, max_length = 500)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    
    class meta:
        verbose_name_plural ="conversations"
        db_table = "conversations"
        
    def __str__(self):
        self.text