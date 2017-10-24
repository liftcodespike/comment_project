from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Comment
from django.contrib import messages

# Create your views here.
def home(request):
	if 'user_first_name' not in request.session:
		return redirect('/')
	context = {
		'other_users': User.objects.exclude(id = request.session['user_id'])
	}
	return render(request, 'main_app/index.html', context)

def showUser(request, id):
	context = {
		'shown_user': User.objects.get(id = id)
	}
	return render(request, 'main_app/show.html', context)

def addComment(request):
	results = Comment.objects.validate(request.POST)
	if len(results['errors']) > 0:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/main/show/'+  request.POST['user_id'])

	Comment.objects.create(content = request.POST['content'], poster = User.objects.get(id = request.POST['poster_id']),user = User.objects.get(id = request.POST['user_id']))
	messages.success(request, 'You have created a comment. You should be so proud. Your kids will not resent you.')
	return redirect('/main/show/'+  request.POST['user_id'])

