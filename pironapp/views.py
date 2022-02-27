from django.shortcuts import render


# Create your views here.
def profile_action(request):
    return render(request, 'profile.html')
