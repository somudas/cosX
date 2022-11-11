from genericpath import exists
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'cosx_home/home.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if  password1 == password2:
            if User.objects.filter(username=username).exists():
                # username already exists
                messages.error(request, "username already exists")
                return render(request, 'cosx_home/register.html')        
            elif User.objects.filter(email=email).exists():
                # email already exists
                messages.error(request, "email already exists")
                return render(request, 'cosx_home/register.html')
            
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=fname, last_name=lname)
            user.save()

            return redirect('login')
        else:
            messages.error(request, "both passwords should match!!")    
    return render(request, 'cosx_home/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('cosx-home')
        messages.error(request, "invalid username/password")
        return redirect('login')


    return render(request, 'cosx_home/login.html')

def logout(request):
    auth.logout(request)

    return redirect("cosx-home")
