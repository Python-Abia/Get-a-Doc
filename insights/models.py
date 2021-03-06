from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InsightsCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "insights_categories"
        verbose_name_plural = "insights categories"


class Insight(models.Model):
    title   = models.CharField(max_length=200, unique=True)  
    slug    = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(InsightsCategory, on_delete=models.CASCADE)
    body    = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='insight_posts')
    postImage = models.ImageField( blank = True)
    updated_on    = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:100] + '...'
    
    class Meta:
        verbose_name_plural = "insights"
        db_table = "insights"
    
    