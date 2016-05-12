from django.shortcuts import render, redirect
import time
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .models import Comment

def index(request):
	return render(request, 'walmart/index.html',)

def login_method(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			un = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			user = authenticate(username=un, password=pw)
			if user is not None:
				if user.is_active:
					login(request, user)
					return JsonResponse({'status':'true','message':'login successful'})
					# Redirect to a success page.
				else:
					# Return a 'disabled account' error message
					return JsonResponse({'status':'false','message':'account not active'})

			else:
				return JsonResponse({'status':'false','message':'invalid username or password'})
				# Return an 'invalid login' error message
		else:
			return JsonResponse({'status':'warn','message':'your form is not valid'})


def logout_method(request):
    logout(request)
    return redirect('/walmart')
    # Redirect to a success page.


@login_required(login_url='/walmart')
def show_presentation(request):
	print('5')

def method(request):
	name_dict = {'sjl': 'Love xyw', 'xyw': 'Love sjl'}
	time.sleep(10)
	return JsonResponse(name_dict)
	

	
