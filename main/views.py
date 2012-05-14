# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from main.forms import UserForm, ContactForm
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
    return HttpResponse("Hello, world. You're out!")

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

        return render_to_response('index.html')
    else:
       return HttpResponse("Invalid")
