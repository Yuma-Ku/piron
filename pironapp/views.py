from django.shortcuts import render


# Create your views here.
def profile_action(request):
    return render(request, 'profile.html')

def demo_action(request):
    return render(request, 'demo.html')

def login_action(request):
    return render(request, 'login.html')