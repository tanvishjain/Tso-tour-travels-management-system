from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib import messages
from .models import Contact, Feedback
from .serializers import *
from .forms import ContactForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from PackageApp.models import Booking, Cancellation

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = feedbackSerializer

def HomePage(request):
    return render(request,'home/index.html')

def AfterHomePage(request):
    return render(request,'home/after_login_index.html')


def AboutusView(request):
    return render(request,'home/aboutus.html')

def AfterAboutusView(request):
    return render(request,'home/after_login_aboutus.html')

@login_required(login_url='/log-page/')
def MyProfile(request):
    user = request.user
    booking = Booking.objects.filter(User=user.id)
    # cancel = Cancellation.objects.filter(User=user.id)
    context = {
        'user' : user,
        'booking' : booking,
        # 'cancel' : cancel
    }
    return render(request,'home/myprofile.html',context)

def ContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Form fill successfully.')
            # return render(request,'home/contact.html')
            return redirect('/contact/')
        
    else:
        form = ContactForm()

    return render(request,'home/contact.html',{'form' : form})

def AfterContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Form fill successfully.')
            # return render(request,'home/contact.html')
            return redirect('/aft-contact/')
        
    else:
        form = ContactForm()

    return render(request,'home/after_login_contact.html',{'form' : form})

@login_required(login_url='/log-page/')
def FeedbackView(request,):

    if request.method == 'POST':
        form = FeedbackForm(request.POST, user = request.user)
        if form.is_valid():
            form.save()
            return redirect('/feedback/')
        
    else:
        form = FeedbackForm()

    return render(request,'home/feedback.html',{'form' : form})

