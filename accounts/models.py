from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
import datetime
# Create your models here.

User = get_user_model()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/')
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    is_doctor = models.BooleanField()
    reg_date  = models.DateTimeField(default = datetime.datetime.now)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name_plural = 'User Profiles'
        db_table = 'user_profiles'