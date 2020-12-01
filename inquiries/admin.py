from django.contrib import admin
from . models import Inquiry, InquiryCategory, Syptoms

# Register your models here.
admin.site.register(Inquiry)
admin.site.register(InquiryCategory)
admin.site.register(Syptoms)

