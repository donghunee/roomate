from django.shortcuts import render
import sys, os
parent_dir = os.path.abspath('..')
sys.path.append(parent_dir)

from main.models import Post
import pandas as pd
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def show_matching(request):
    data = {}
    current_user = request.user.username
    user = User.objects.get(username=current_user)
    post = get_object_or_404(Post, user=user)

    all_data = Post.objects.all()

    if post.sex == 'male':
        sex_filter1 = all_data.filter(sex = 'male')
        # 흡연 필터 추가해야함
    else:
        sex_filter2 = all_data.filter(sex = 'female')

    return render(request, 'show_matching.html', data)
