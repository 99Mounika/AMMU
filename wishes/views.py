from django.shortcuts import render, redirect
#from wishes.forms import UserForm,Userlogin
from django.http import HttpResponse

# Create your views here.
def firstpage(request):
	return render(request, 'wishes/firstpage.html')


def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		if username == "mk" and password == "mo123":
			return render(request,'wishes/home.html')
		else:
			return HttpResponse("wrong credentaials")

	return render(request, 'wishes/login.html')

'''def home(request):
	return render(request,'wishes/home.html')'''