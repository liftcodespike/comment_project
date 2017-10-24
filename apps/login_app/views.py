from django.shortcuts import render, redirect
from models import User
from django.contrib import messages



def index(request):
	return render(request, 'login_app/index.html')

def register(request):
	results =  User.objects.regVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	user = User.objects.creator(request.POST)
	messages.success(request, 'User has been created. Please log in to continue.')
	return redirect('/')

def login(request):
	results = User.objects.logVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['user_id'] = results['user'].id
	request.session['user_first_name'] = results['user'].first_name
	return redirect('/main/home')



def logout(request):
	request.session.flush()
	return redirect('/')





