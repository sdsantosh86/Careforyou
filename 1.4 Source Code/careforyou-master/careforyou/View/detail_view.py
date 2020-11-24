from django.shortcuts import render
from careforyou.Model.models import Childcare, Quality
import careforyou.API.reivews as rvtool
import careforyou.API.language_tool as lt
import math
import time


def program_exists(cid):
    childcare = Childcare.objects.filter(id=cid)
    if childcare[0].program_id.type == "No Program":
        return False
    else:
        return True


def get_rating(cid):
    quality = Quality.objects.filter(childcare_id__id=cid)
    # if childcare has no quality
    if len(quality) == 0:
        return None
    area = [0] * 8
    for i in range(len(quality)):
        area[0] = area[0] + quality[i].area1
        area[1] = area[1] + quality[i].area2
        area[2] = area[2] + quality[i].area3
        area[3] = area[3] + quality[i].area4
        area[4] = area[4] + quality[i].area5
        area[5] = area[5] + quality[i].area6
        area[6] = area[6] + quality[i].area7
        area[7] = area[7] + quality[i].overall
    for i in range(len(area)):
        area[i] = area[i]/len(quality)
    return area


def get_view(request):
    lt.change_language(request)
    if request.method == 'GET':
        para = dict(request.GET)
        cid = para['id'][0]
        childcare = Childcare.objects.filter(id=cid)
        rating = get_rating(cid)
        # if childcare has no quality
        if rating is None:
            quality_exist = False
            empty_stars = 0
            quality_stars = 0
        else:
            quality_exist = True
            empty_stars = math.ceil(5-rating[7])
            quality_stars = int(rating[7])
        # program exists
        program_exist = program_exists(cid)
        # get reviews
        reviews = get_reviews_by_name(childcare[0].name)
        reviews_exist = True
        if reviews is None:
            reviews_exist = False
    context = {'childcare': childcare[0],
               'rating':rating,
               'empty_star':empty_stars,
               'quality_star':quality_stars,
               'program_exist': program_exist,
               'quality_exist': quality_exist,
               'reviews_exist': reviews_exist,
               'reviews':reviews
               }
    return render(request, 'detail.html', context)


def get_reviews_by_name(name):
    place_id = rvtool.get_place_id(name+',Victoria')
    if place_id is None:
        return None
    reviews = rvtool.get_reviews(place_id[0]['place_id'])
    if reviews is None:
        return None
    for i in range(len(reviews)):
        reviews[i]['time'] = time.strftime("%d-%m-%Y", time.localtime(reviews[i]['time']))
    return reviews


def if_saved(cid):
    pass