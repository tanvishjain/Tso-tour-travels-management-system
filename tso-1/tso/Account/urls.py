from django.contrib import admin
from django.urls import path, include
from Account import views
from home.views import HomePage
from .views import *

urlpatterns = [
    path('',views.signup,name="signup"),
    path('log-page/',views.LoginPage,name="log-page"),
    path('change-pass/',views.ChangePassword,name="change-pass"),
    path('aft-signup/',views.AfterSignup,name="aft-signup"),
    path('aft-log-page/',views.AfterLoginPage,name="aft-log-page"),
    path('aft-change-pass/',views.AfterChangePassword,name="aft-change-pass"),
]