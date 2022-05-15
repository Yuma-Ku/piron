from django.shortcuts import render


# Create your views here.
def profile_action(request):
    return render(request, 'profile.html')

def post_action(request):
    return render(request, 'post-post.html')

def login_action(request):
    return render(request, 'login.html')