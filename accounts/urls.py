from django.urls import path
from .import views

# named url
account_name = 'accounts'

urlpatterns = [
    path('', views.index, name ='index'),
    path('login', views.Userlogin, name ='login'),
    path('logout', views.Userlogout, name ='logout')
]