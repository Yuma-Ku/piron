from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from pironapp.models import User

# Create your views here.
def profile_action(request):
    return render(request, 'profile.html')

def post_action(request):
    return render(request, 'post-post.html')

@csrf_exempt
def login_action(request):

    # Sample db filter (SELECT query)
    user = User.objects.filter(name="Benson")

    args = {}
    next_page = "login.html"

    if (request.method == 'POST'):

        if request.POST.get("login_id") == "" and request.POST.get("login_pass") == "":
            text = 'Enter your login details.'
        else:
            if request.POST.get("login_id") == "":
                text = 'Enter your login ID.'
            elif request.POST.get("login_pass") == "":
                text = "Enter your password."
            else:
                text = 'Incorrect email or password.'
                next_page = 'profile.html'    
                return HttpResponseRedirect("/profile/")
        
        args['error_message'] = text
        args['login_id'] = request.POST.get("login_id")
    else:
        # Initial setting from db
        args['login_id'] = user[0].email

    # return render(request, 'login.html')
    return render(request, next_page, args)