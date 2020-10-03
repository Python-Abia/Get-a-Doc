from django.db import models

# Create your models here.
class Conversation(models.Model):
    first_name = models.CharField(blank =False, max_length = 50) 
    last_name  = models.CharField(blank =False, max_length = 50)
    subject    = models.CharField(blank =False, max_length = 20) 
    email      = models.EmailField(blank =False, max_length = 50)
    text       = models.TextField(blank =False, max_length = 500)
    
    
    class meta:
<<<<<<< HEAD
        verbose_name_plural ="conversations"
        db_table = "conversations"
=======
        verbose_name_plural ="messages"
        db_table = "messages"
>>>>>>> 9685caf2b3a34308bc58ce04c2baa3a1b023f3c3
        
    def __str__(self):
        return self.email + " " + self.subject