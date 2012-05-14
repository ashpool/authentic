# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from main.forms import UserForm
from main.models import UserLogin

@login_required(login_url='/accounts/login/')
def home(request):
    user = request.user
    userlogins=UserLogin.objects.filter(user=user).order_by('timestamp') #filter(user = user)

    if len(userlogins) > 5:
        userlogins = userlogins[:5]

    userlogins.reverse()

    return render_to_response('index.html', {'user':user, 'userlogins': userlogins})

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/loggedout/")

def loggedout(request):
    return HttpResponseRedirect("/")

def register(request):
    form = UserForm()
    c = {'form': form}
    c.update(csrf(request))
    return render_to_response('register.html', c)

def create_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.instance
        user.set_password(user.password)
        user.save()

        return HttpResponseRedirect("/")

