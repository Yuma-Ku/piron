from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from pironapp.models import Post, User
from .forms import LoginForm
from django.urls import resolve
import os
import datetime

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
    
    user = User.objects.get(pk=request.session.get('user_id'))
    featured_post = Post.objects.get(pk=15)
    posts = Post.objects.filter(user_id=user.id)
    
    # return HttpResponse(posts.location)
    
    args = {
        'title': 'ホーム',
        'user': user,
        'featured_post': featured_post,
        'posts': posts
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
    
    if (request.method == 'POST'):
        params = request.POST
        # title = request.POST.get("post-image-drop")
        # return HttpResponse(params["post-title"])
        
        
        post_obj = Post()
        post_obj.title = params["post-title"]
        post_obj.description = params["post-description"]
        post_obj.location = params["post-location"]
        
        
        if request.FILES.get("post-image-drop", None) is not None:
            # sample = Sample(name="Benson", image = request.FILES["post-image-drop"])
            # sample.save()
            # So this would be the logic
            img = request.FILES["post-image-drop"]
            img_extension = os.path.splitext(img.name)[1]

            # This will generate random folder for saving your image using UUID
            # save_path = ""
            # i
            # 
            # 
            # 
            # 
            # 
            # 
            # 
            # f not os.path.exists(save_path):
            #     # This will ensure that the path is created properly and will raise exception if the directory already exists
            #     os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Create image save path with title
            MEDIA_IMAGE_PATH = "media/images/"
            date_now = datetime.datetime.now()
            img_name = "tmb_img_%s" % (date_now.strftime("%Y%m%d%H%M%S"))
            img_save_path = "%s%s.%s" % (MEDIA_IMAGE_PATH, img_name, img_extension)
            with open(img_save_path, "wb+") as f:
                for chunk in img.chunks():
                    f.write(chunk)
            # args["success"] =  True
            post_obj.thumbnail_image = img_save_path
            # return HttpResponse(img_save_path)
            
            
        else:
            # return JsonResponse(data)
            return HttpResponse("ha?")
        
        post_obj.save()
            
    
    
    return render(request, 'create/post.html', args)

def create_live_action(request):
    args = {
        'title': 'ポスト作成',
    }
    return render(request, 'create/live.html', args)