from django.shortcuts import render


# Create your views here.
def profile_action(request):
    return render(request, 'profile.html')

def post_action(request):
    return render(request, 'post-post.html')

def message_action(request):
    return render(request, 'message.html')
