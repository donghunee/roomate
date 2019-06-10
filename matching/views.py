from django.shortcuts import render
import sys, os
parent_dir = os.path.abspath('..')
sys.path.append(parent_dir)

from main.models import Post
import pandas as pd
import numpy as np
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from scipy.spatial import distance_matrix


def show_matching(request):
    data = {}
    current_user = request.user.username
    user = User.objects.get(username=current_user)
    post = get_object_or_404(Post, user=user)



    all_data = Post.objects.all()

    # 성별 필터링 결과
    filter_data=sex_filter(post, all_data)
    data['sex_filter'] = filter_data
    # filter_result에는 자기 자신 또한 포함됨

    # 청결 점수 만들기
    clean_point=make_clean_point(post, filter_data)
    data['clean_point'] = clean_point

    # # 라이프 사이클 점수 만들기
    # # 왜 안되는지 모르겠음
    # life_point=make_life_point(post, filter_data)
    # data['life_point'] = life_point

    # 성격 점수 만들기
    situation_point=make_situation_point(post, filter_data)
    data['situation_point'] = situation_point

    # 점수 합산하기
    matching_result = sum_point(post, filter_data, clean_point, situation_point)
    data['matching_result'] = matching_result
    print(type(matching_result))


    return render(request, 'show_matching.html', data)



    # 성별 필터링 함수
def sex_filter(post, all_data):
    if post.sex == 'male':
        sex_filter = all_data.filter(sex = 'male')
        return(sex_filter)

    else:
        sex_filter = all_data.filter(sex = 'female')
        return(sex_filter)

def make_clean_point(post, filter_data):
    clean_sector = pd.DataFrame(list(filter_data.all().values('shoes', 'toilet', 'kitchen', 'room')))
    name = pd.DataFrame(list(filter_data.all().values('user_id')))
    dist_matrix = pd.DataFrame(distance_matrix(clean_sector.values, clean_sector.values), index=name.user_id, columns=name.user_id)
    clean_point=round((1/(dist_matrix+1))*2,3)
    target_code=post.user_id
    clean_point=pd.DataFrame(clean_point[target_code])
    return (clean_point)

################## 계속된 에러로 일단 포기 ################
def make_life_point(post, filter_data):
    orginal_life = pd.DataFrame(list(filter_data.all().values('pattern')))
    name = pd.DataFrame(list(filter_data.all().values('user_id')))
    target_code=post.user_id


    a=np.array([orginal_life['pattern']])
    b=np.array([orginal_life['pattern']]).T

    life_point=pd.DataFrame(a+b, index=name.user_id, columns=name.user_id)
    life_target=pd.DataFrame(life_point[target_code])
    life_set = {('AAAA', 'AAAx', 'AaaA','Aaax','axax','AxAx','aAAx','AxAA','AxaA','axaa','AaaA','aAAa'):1, #완벽 일치
            ('AAAa', 'AAaA', 'AaAA', 'AaAx','aAax','AaAx','AxAa','aAaa'):0.66, #한명의 니즈는 맞춤, 생활 타입 동일
            ('AAax','Aaaa','Axaa','axAA','axaA','Aaaa','aAAA' ):0.33, #한명의 니즈는 맞춤, 생활 타입 다름
            ('AaAa', 'aAaA'):0.33, #한명의 니즈도 맞추지 못함, 생활 타입은 같음
            ('AAaa', 'aaAA'):0 #한명의 니즈도 맞추지 못함, 생활 타입도 다름
           }
    #
    life_list = [0 for i in range(len(life_target))]
    # for i in range(len(life_target[target_code])):
    #     print(life_target[0])
    #     for key in life_set:
    #         print('right')
            # if life_target[target_code][i] in key:
            #     print('right')
            #     # life_list[i] = life_set[key]
    # life_target.insert(loc=1, column='point', value=life_list)

    return(life_list)
##################################################
def make_situation_point(post, filter_data):
    target_code=post.user_id
    origin_data = pd.DataFrame(list(filter_data.all().values('user_id', 'one','two','thr')))

    target_char_value = origin_data[origin_data['user_id'] == target_code]

    situation_point = [0 for i in range(len(origin_data))]

    for i in range(len(origin_data)):
        if origin_data['one'][i] == target_char_value['one'].item():
            situation_point[i] += 0.33

        if origin_data['two'][i] == target_char_value['two'].item():
            situation_point[i] += 0.33

        if origin_data['thr'][i] == target_char_value['thr'].item():
            situation_point[i] += 0.33

        # relation_point는 차이의 역수, 내 생각에는 차이가 크면 더 가중치를 주고 싶은데 일단 그냥 진행한다.
    return(situation_point)

def sum_point(post, filter_data, clean_point, situation_point):
    target_code=post.user_id
    origin_data = pd.DataFrame(list(filter_data.all().values('user_id')))
    result_list = []
    for i in range(len(clean_point[target_code])):
        result_list.append(list(clean_point[target_code])[i]  + list(situation_point)[i])


    result=pd.DataFrame()
    result['user_id'] = origin_data['user_id']
    result['point'] = result_list
    result['point'] = result['point'].apply(lambda x: (x-min(result_list))/(max(result_list)-min(result_list)))
    result['clean_point'] = list(clean_point[target_code])
    result['situation_point'] = list(situation_point)

    result = result.sort_values(by='user_id', ascending=True)
    result = result.reset_index(drop = True)


    point_list = []
    for i in range(len(result['point'])):
        temp = {}
        temp['user_id'] = result.loc[i]['user_id']
        temp['point'] = result.loc[i]['point']
        temp['clean_point'] = result.loc[i]['clean_point']
        temp['situation_point'] = result.loc[i]['situation_point']
        point_list.append(temp)



    return(point_list)
