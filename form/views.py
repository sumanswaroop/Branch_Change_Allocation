from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf 
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

from form.forms import userpostform
# Create your views here.


def bchangeform(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	return render(request, 'form.html', {'form': userpostform() })


def login(request):
	c={}
	c.update(csrf(request))
	if request.user.is_authenticated():
		return HttpResponseRedirect('/bchangeform')
	return render_to_response('home.html', c, context_instance= RequestContext(request))


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password =password )

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/bchangeform')
	else:
		messages.error(request, 'Username or Password is not valid')
		return HttpResponseRedirect('/login')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html',{})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login')
		else:
			messages.error(request, 'Passwords Donot Match')
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	return render_to_response('register.html',args,context_instance=RequestContext(request))

 