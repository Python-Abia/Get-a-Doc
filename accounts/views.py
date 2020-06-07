from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout

# Create your views here.

def index(request):
    if request.method ==  'POST':
        form = UserRegistrationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect(login)
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/index.html', {'form':form})



def Userlogin(request):
    return render(request, 'accounts/login.html')



def Userlogout(request):
    return render(request, 'accounts/logout.html')

