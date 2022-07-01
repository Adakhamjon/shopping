from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login 
from .forms import UserRegisterForm,UserLogInForm
from .models import User
def register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()

	context = {
	"form":form
	}
	return render(request,"register.html",context)
def login_account(request):
	form = UserLogInForm()
	if request.method =="POST":
		form = UserLogInForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			user = authenticate(request,email=email,password=password)
			if user:
				login(request,user=user)
				return redirect(reverse("store-page"))
			else:
				print("xato")
	context = {
	"form":form
	}
	return render(request,"login.html",context)
