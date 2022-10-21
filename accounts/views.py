from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms, decorators

# Create your views here.
@decorators.unauthenticated
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user != None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username OR Password is incorrect')
	context = {'form' :'form'}
	return render(request, 'accounts/login.html', context)

def logout_user(request):
	logout(request)
	return redirect('accounts:login')

def registerPage(request):
	form = forms.MemberForm

	if request.method == 'POST':
		print('posted')
		form = forms.MemberForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('accounts:login')

	context = {'form':form}
	return render(request, 'accounts/register.html', context)


def register_request(request):
	if request.method == "POST":
		form = forms.MemberForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = forms.MemberForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

@login_required(login_url='accounts:login')
def profile(request):
	pass