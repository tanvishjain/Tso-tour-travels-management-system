from django.contrib import admin
from django.urls import path, include
from home import views
from Account.views import signup, LoginPage, LogoutPage, AfterLoginPage, AfterSignup
from .views import *

urlpatterns = [
    path('',views.HomePage,name="home-page"),
    path('about-us/',views.AboutusView,name="about-us"),
    path('contact/',views.ContactView,name="contact"),
    path('feedback/',views.FeedbackView,name="feedback"),
    path('signup/',signup,name="signup"),
    path('my-profile/',views.MyProfile,name="my-profile"),
    path('log-page/',LoginPage,name="log-page"),
    path('log-out/',LogoutPage,name="log-out"),
    path('aft-home-page',views.AfterHomePage,name="aft-home-page"),
    path('aft-about-us/',views.AfterAboutusView,name="aft-about-us"),
    path('aft-contact/',views.AfterContactView,name="aft-contact"),
    path('aft-signup/',AfterSignup,name="aft-signup"),
    path('aft-log-page/',AfterLoginPage,name="aft-log-page"),
]