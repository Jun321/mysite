from django.shortcuts import render, redirect
import time
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .models import Comment

def index(request):
	form = UserForm()
	return render(request, 'walmart/index.html', {'form': form})

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
					return JsonResponse({'status':'true','message':'login_success'}, status=200)
					# Redirect to a success page.
				else:
					# Return a 'disabled account' error message
					return JsonResponse({'status':'false','message':'not_active'}, status=200)

			else:
				return JsonResponse({'status':'false','message':'no_user'}, status=200)
				# Return an 'invalid login' error message
		else:
			return JsonResponse({'status':'false','message':'form_is_not_valid'}, status=500)

def logout(request):
    logout(request)
    # Redirect to a success page.


@login_required
def show_presentation(request):
	print('5')

def method(request):
	name_dict = {'sjl': 'Love xyw', 'xyw': 'Love sjl'}
	time.sleep(10)
	return JsonResponse(name_dict)
	

	
