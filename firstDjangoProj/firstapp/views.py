from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.
def machine(request):
    return HttpResponse("Hello MC")

def login_user(request):
    return render(request,"user_reg.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form} )
    