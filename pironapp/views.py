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
    
    if (request.session.get('id', False)):
        # return HttpResponse(request.session["id"])
        return render(request, 'home/index.html')

    if (request.method == 'POST'):
        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            request.session["id"] = 123
            return render(request, 'home/index.html')
    else:
        login_form = LoginForm()

    args = {
        'form': login_form,
    }

    return render(request, 'login/index.html', args)

def logout_action(request):
    del request.session['id']
    return HttpResponseRedirect('/')
    