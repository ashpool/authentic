# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from main.models import UserLogin

@login_required(login_url='/accounts/login/')
def home(request):
    user =  User(username = 'magnus')


    userlogins=UserLogin.objects.all().order_by('timestamp') #filter(user = user)

    if len(userlogins) > 5:
        userlogins = userlogins[:5]

    userlogins.reverse()

    return render_to_response('index.html', {'user':user, 'userlogins': userlogins})

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/loggedout/")

def loggedout(request):
    return HttpResponse("Hello, world. You're out!")