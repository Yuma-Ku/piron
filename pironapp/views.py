from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm


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


@csrf_exempt
def login_action(request):

    # Sample db filter (SELECT query)
    # user = User.objects.filter(name="Benson")
    args = {}

    if (request.method == 'POST'):

        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            # return HttpResponse("valid")
            return HttpResponseRedirect('/home')
        # else:
            # return HttpResponse("invalid")

        # if request.POST.get("login_id") == "" and request.POST.get("login_pass") == "":
        #     text = 'Enter your login details.'
        # else:
        #     if request.POST.get("login_id") == "":
        #         text = 'Enter your login ID.'
        #     elif request.POST.get("login_pass") == "":
        #         text = "Enter your password."
        #     else:

        #         count_1 = is_login_valid(request.POST.get("login_id"), request.POST.get("login_pass"))
        #         return HttpResponse(str(count_1))

        #         text = 'Incorrect email or password.'
        #         # next_page = 'home.html'
        #         return HttpResponseRedirect("/home/")

        # args['error_message'] = text
        # args['login_id'] = request.POST.get("login_id")
    else:
        login_form = LoginForm()
        # Initial smethodetting from db
        # args['login_id'] = user[0].email

    args['form'] = login_form

    # return render(request, 'login.html')
    return render(request, 'login/index.html', args)


def home_action(request):
    return render(request, 'home.html')
