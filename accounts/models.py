from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserProfile:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/')
    address = models.TextField()
    phone = models.CharField(max_length=30)
    is_doctor = models.BooleanField()
    reg_date  = models.DateTimeField(default = datetime.datetime.now)

    def __str__(self):
        return user.first_name + " " + user.last_name

    class Meta:
        verbose_name_plural = 'User Profiles'
        db_table = 'user_profiles'



