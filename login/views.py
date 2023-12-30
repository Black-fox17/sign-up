from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from .forms import sign_in,login_web
from .models import new_page
# Create your views here.
def home(request):
    return render(request,"login/home.html")
def sign_up(request):
    form = sign_in
    if request.method == "POST":
        form = sign_in(request.POST)

        if form.is_valid():
            print("Valid form")
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email = form.cleaned_data['Email']
            obj = new_page(Username = username,Password = password,Email = email)
            obj.save()
            return redirect('/login/congrat')
        else:
            form = sign_in()
    return render(request,"login/sign_up.html",{'form':form})
def congrat(request):
    return render(request,"login/congratulation.html")
def log_inn(request):
    form = login_web
    if request.method == "POST":
        form = login_web(request.POST)

        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            print(f"Username is {username}")
            print(f"Password is {password}")
            try:
                user = new_page.objects.get(Username = username)
                print(user == username)
                print(user.Password == password)
            except new_page.DoesNotExist:
                user = None
            if user and user.Password == password:
                print("Correct")
                return redirect('/login/success')
            else:
                print("Not correct")
                return render(request,"login/login.html",{'form':form,"error":"Invalid credentials"})
    return render(request,"login/login.html",{'form':form})
def success(request):
    return render(request,"login/success.html")