from django.shortcuts import render, redirect
import time
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Comment

def index(request):
	return render(request, 'walmart/index.html', )

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('walmart/index.html')
			# Redirect to a success page.
		else:
		# Return a 'disabled account' error message
			print('1')

	else:
		print('2')
	# Return an 'invalid login' error message.

def logout(request):
    logout(request)
    # Redirect to a success page.


@login_required
def show_presentation(request):
	print('5')

def method(request):
	name_dict = {'sjl': 'Love xyw', 'xyw': 'Love sjl'}
	return JsonResponse(name_dict)
	
