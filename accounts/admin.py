from django.contrib import admin
from .models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_doctor')    # The value of 'list_display' must not be a ManyToManyField.
    list_filter = ('is_doctor',)    # The value of 'list_filter' must be a list or tuple
    search_fields = ('user',)
    ordering = ('user',)