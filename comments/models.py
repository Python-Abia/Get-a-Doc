from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.git
class Comment(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False, max_length = 500)
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    
    
    class Meta:
        verbose_name_plural ="comments"
        db_table = "comments"
        
    def __str__(self):
        self.text