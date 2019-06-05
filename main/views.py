from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# 새로 추가하는 메소드
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text

from .models import Post

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['Password1'] == request.POST['Password2']:
            user = User.objects.create_user(
                request.POST['username'],email=request.POST['Email1'], password=request.POST['Password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('user_activate_email.html', 						{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = "[나랑살자] 회원가입 인증 메일입니다."
            user_email = request.POST['Email1']
            email = EmailMessage(mail_subject, message, to=[user_email])
            email.send()
            return render(request,'email.html')
            #auth.login(request, user)
    return render(request,"signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_id',None)
        password = request.POST.get('user_pw',None)
        username = request.POST['user_id']
        password = request.POST['user_pw']
        

        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('index') 
            else:
                return render(request,'index.html',{"error":"이메일을 인증해주세요."})
        else:
            #messages.add_message(request, messages.INFO, '새 글이 등록되었습니다.') 

            messages.info(request, '아이디와 비밀번호를 확인 해주세요.') #     두번째, shortcut 형태
            return redirect('index')
            #return render(request,'index.html',{"error":"아이디와 비밀번호를 확인해 주세요"})
    else:
        return render(request, 'index.html')

def activate(request, uid64, token):
    
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return render(request,'index.html',{'alert':'이메일이 인증되었습니다.'})
    else:
        return HttpResponse('비정상적인 접근입니다.')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'index.html')



def first(request):
    if  request.method == "POST":
        current_user = request.user.username
        user=User.objects.get(username=current_user)
        post = get_object_or_404(Post, user=user)
        if post == None:
            post = Post()
            post.user = user
            post.sex = request.POST["sex"]
            post.smoke = request.POST["smoke"]
            post.shoes = request.POST["shoes"]
            post.kitchen = request.POST["kitchen"]
            post.room = request.POST["room"]
            post.toilet = request.POST["toilet"]
            post.save()
        else:          
            post.user = user
            post.sex = request.POST["sex"]
            post.smoke = request.POST["smoke"]
            post.shoes = request.POST["shoes"]
            post.kitchen = request.POST["kitchen"]
            post.room = request.POST["room"]
            post.toilet = request.POST["toilet"]
            post.save()
        return redirect('two')
    return render(request,'wash.html')


def two(request):
    if request.method == "POST":
        current_user = request.user.username
        user = User.objects.get(username=current_user)
        post = get_object_or_404(Post, user=user)
        print(user)
        post.room_in = request.POST['room_in']
        post.sleep = request.POST['sleep']
        post.save()
        if request.POST['sleep'] == "3":
            return render(request,'three.html',{'day':'야간형'})
        else:
            return render(request,'three.html',{'day':'주간형'})
    return render(request,'two.html')


def three(request):
    if request.method == "POST":
        current_user = request.user.username
        user = User.objects.get(username=current_user)
        post = get_object_or_404(Post, user=user)
        post.roomate = request.POST["roomate"]
        post.save()
        return render(request,'four.html')
    return render(request,'four.html')

def four(request):
    if request.method == "POST":
        current_user = request.user.username
        user = User.objects.get(username=current_user)
        post = get_object_or_404(Post, user=user)
        post.one = request.POST["one"]
        post.two = request.POST["two"]
        post.thr = request.POST["three"]
        post.save()
        return render(request,'fin.html')

def fin(request):
    return render(request,'fin.html')

def ema(request):
    return render(request,'email.html')