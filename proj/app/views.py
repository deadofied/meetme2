from django.shortcuts import render, get_object_or_404
from app.models import Profile, Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import string
import random

@login_required 
def newsfeed(request):
    if (request.GET.get('q', '') == ''):
        profiles = Profile.objects.filter(active=True)
    else:
        profiles = Profile.objects.filter(interests__icontains=request.GET.get('q', ''))
    return render(request, 'app/newsfeed.html', {'profiles': profiles})
 
@login_required 
def profile(request, slug):
    user = get_object_or_404(User, username=slug)
    return render(request, 'app/profile.html', {'profile': user.get_profile(), 'user': user})

def index(request):
    return render(request, 'app/index.html', {})

def aboutus(request):
    return render(request, 'app/aboutus.html', {})

def loginview(request):
    return render(request, 'app/loginview.html', {})    

@login_required
def home(request):
    events = Event.objects.all()
    return render(request, 'app/home.html', {'events': events})    

@login_required 
def home(request):
    if (request.GET.get('q', '') == ''):
        events = Event.objects.all()
    else:
        events = Event.objects.filter(Q(interests1__icontains=request.GET.get('q', '')) | Q(interests2__icontains=request.GET.get('q', '')))
    return render(request, 'app/home.html', {'events': events})

@login_required
def edit(request):
        return render(request,'app/edit.html',{'user': request.user, 'profile': request.user.get_profile()})     

def register(request):
    return render(request, 'app/register.html', {})

def deauthorize(request):
    logout(request)
    return HttpResponseRedirect('../')	


@login_required
def newevent(request):
    description = request.POST['description']
    title = request.POST['title']
    interests1 = request.POST['interests1']
    interests2 = request.POST['interests2']
    slug = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    Event.objects.create(description = description, title = title, interests1 = interests1, interests2 = interests2);
    return HttpResponseRedirect('../home')		


def authorize(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
			login(request, user)
			return HttpResponseRedirect('../home')			
        else:
            print('account disabled, sorry!')
    else:
        print('oops, wrong login')
        return HttpResponseRedirect('../')			

