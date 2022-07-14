from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm
from django.urls import resolve


def profile_action(request):
    return render(request, 'profile.html')


def post_action(request):
    return render(request, 'post-post.html')


def register_action(request):
    return render(request, 'register.html')


def register2_action(request):
    return render(request, 'register-2.html')


def register3_action(request):
    return render(request, 'register-3.html')


def login_action(request):
    
    if (request.session.get('user_id', False)):
        return HttpResponseRedirect('/')
    
    login_form = LoginForm()
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            request.session['user_id'] = login_form.cleaned_data['user_id']
            return HttpResponseRedirect('/')

    args = {
        'form': login_form,
        'url_name': 'login',
    }

    # return HttpResponse(request.resolver_match.url_name)
    return render(request, 'login/index.html', args)

def home_action(request):
    if (not request.session.get('user_id', False)):
        return HttpResponseRedirect('/login/')
    # return HttpResponse(request.resolver_match.url_name)
    
    return render(request, 'home/index.html')
        
    

def logout_action(request):
    if (request.session.get('user_id', False)):
        del request.session['user_id']
    return HttpResponseRedirect('/')
    