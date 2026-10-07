from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm, AuthenticationForm

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

def HomePage(request):
    return render(request,'home/index.html')

def signup(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log-page')
    else:
        form = CustomUserCreationForm()

    context = {'form' : form}
    return render(request,'Account/signup.html',context)

def AfterSignup(request):

    form = CustomUserCreationForm 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aft-log-page/')

    context = {'form' : form}
    return render(request,'Account/after_login_signup.html',context)

def LoginPage(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return render(request,'home/after_login_index.html')

    return render(request,'Account/login.html',{'form' : form})

def AfterLoginPage(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return render(request,'home/after_login_index.html')

    return render(request,'home/after_login_index.html',{'form' : form})

def LogoutPage(request):
        logout(request)
        return redirect('/log-page/')

def ChangePassword(request):
        
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Your Password has been changed successfully....')
                return render(request,'Account/login.html')
        else:
            form = PasswordChangeForm(user=request.user)

        return render(request,'Account/changepassword.html',{'form':form})

def AfterChangePassword(request):
        
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Your Password has been changed successfully....')
                return redirect('/aft-log-page/')
        else:
            form = PasswordChangeForm(user=request.user)

        return render(request,'Account/after_login_changepassword.html',{'form':form})