from django.urls import path
from . import views
 
urlpatterns=[
    
    path('chats/', views.conversation_view, name='chats'),
    path('chatform/', views.conversation_form, name='chatform'),
    
]