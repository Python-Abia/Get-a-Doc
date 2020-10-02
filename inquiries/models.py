from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InquiryCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "inquiries_categories"
        verbose_name_plural = "inquiries categories"

class Syptoms(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


    class Meta:
        db_table = "symptoms"
        verbose_name_plural = "symptoms"

class Inquiry(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(InquiryCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "inquiries"
        verbose_name_plural = "inquiries"








    