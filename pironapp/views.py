from django.shortcuts import render
from pironapp.models import User, UserFollower


# Create your views here.
def profile_action(request):
    user_info = User.objects.get(id=3)
    followers_count = UserFollower.objects.filter(user_id__exact=1).count()
    response = {
        'user_info': user_info,
        'followers_count': followers_count
    }
    
    return render(request, 'profile.html', response)

def post_action(request):
    return render(request, 'post-post.html')

def message_action(request):
    return render(request, 'message.html')
