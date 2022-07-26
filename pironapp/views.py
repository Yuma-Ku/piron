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
        'title': 'ログイン',
    }

    return render(request, 'login/index.html', args)

def home_action(request):
    if (not request.session.get('user_id', False)):
        return HttpResponseRedirect('/login/')
    
    args = {
        'title': 'ホーム',
    }
    
    return render(request, 'home/index.html', args)
        

def logout_action(request):
    if (request.session.get('user_id', False)):
        del request.session['user_id']
    return HttpResponseRedirect('/')
    
def create_action(request):
    
    args = {
        'title': 'ポスト・ライブ',
    }
    
    return render(request, 'create/index.html', args)
    

def create_post_action(request):
    args = {
        'title': 'ポスト作成',
    }
    return render(request, 'create/post.html', args)

def create_live_action(request):
    args = {
        'title': 'ポスト作成',
    }
    return render(request, 'create/live.html', args)