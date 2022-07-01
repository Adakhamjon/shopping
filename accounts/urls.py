from django.urls import path
from .views import*
urlpatterns = [
    path("register/",register,name="register-form"),
    path("login/",login_account,name= "log-in")
]