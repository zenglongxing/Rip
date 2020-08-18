from django.shortcuts import render
from crawl.crawl_method import get_hot_actor as gta
from crawl.crawl_method import *
from webui.utils.Result import ok, error
from django.http import HttpResponse
from webui.utils.vlcUtil import VLC_Player


# Create your views here.


def get_hot_actor(request):
    ret = gta()
    if ret:
        return HttpResponse(ret)
    else:
        return HttpResponse("ok")


def get_movie(request):
    get_movie_by_actor()
    return HttpResponse("爬取成功!")


def get_login(request):
    login()
    return HttpResponse("爬取成功!")


def get_describe(request):
    get_desc()
    return HttpResponse("ok")


def get_photo(request):
    get_photo_method()
    return HttpResponse("ok")


def get_source(request):
    get_community()
    return HttpResponse("ok")


def get_login(request):
    login()
    return HttpResponse("ok")


def get_path(request):
    if request.method == 'GET':
        video_id = request.GET.get('videoId')
        path = get_video_path(video_id)
        # vlc = VLC_Player(path['full_path_url'])
        # vlc.start()
        return ok(path)
    else:
        return error('只支持get方法')
