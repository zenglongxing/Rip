# -*- coding:utf-8 -*-
# @File  : pear/crawl_method.py
# @Author: zlx
# @Date  : 2020-06-26 15:40
# @Desc  : 机器学习
# 代码神兽
#  ┏┓　　　┏┓
# ┏┛┻━━━┛┻┓
# ┃　　　　　　　┃ 　
# ┃　　　━　　　┃
# 　┳┛　┗┳　┃
# 　　　　　　　┃
# 　　　┻　　　┃
# 　　　　　　　┃
# ┗━┓　　　┏━┛
# 　　┃　　　┃神兽保佑
# 　　┃　　　┃代码无BUG！
# 　　┃　　　┗━━━┓
# 　　┃　　　　　　　┣┓
# 　　┃　　　　　　　┏┛
# 　　┗┓┓┏━┳┓┏┛
# 　　　┃┫┫　┃┫┫
# 　　　┗┻┛　┗┻┛
import requests
import json
from requests.utils import dict_from_cookiejar
from crawl.models import *
import pickle
import uuid
import time
import subprocess

headers = {
    'Host': 'm.pearkin.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; FIG-AL10 Build/HUAWEIFIG-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'X-Requested-With': 'com.pear.hot',
}
PREFIX = 'https://m.pearkin.com/api/'


def login():
    login_headers = {
        'Connection': 'keep-alive',
        'Host': 'm.pearkin.com',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'X-Requested-With': 'com.pear.hot',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://m.pearkin.com/vueLogin',
        'Origin': 'https://m.pearkin.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors'
    }
    data = {
        'CU': 'movie-app',
        'CT': '1597668656143',
        'CI': 'QdG5PCudXYhXY+pq5uezj5hxDYByPzh0mFeJOqvW01hIETz7K9RUqBcBjubs73BU33buPRa45MEJE7elKIkkPkcBQLRcuNLY7o/Kyzw38f7xu0z5LUkFS0/u+Zh1A58NBozJLLKiy3TSyT3zV2LONS8sexP5LpPUw72zMAcBeKw=',
        'CV': '10',
        'CP': '2.0.5',
        'CR': '/data/user/0/com.pear.hot/files',
        'appStartCount': '1'
    }
    pre_url = 'https://m.pearkin.com/vueLogin'
    url = "https://m.pearkin.com/api/account/vuelogin"
    cookie = get_cookie()
    if not cookie:
        cookie = {
            'NewPro.LabelCookie': '0',
            '.Pear.Cookies': 'klI2aAox_Q48n4XNIsBGY0vTr-mDkl_PjzI_azx8uc0iSJC--X3cNYT-3x-vt_GIl8eDIMOhqNa1LJPdMUmxnc2sr2Q-UOI1h_mz6D8Z7siEklNGzg7r6wFe_s8KwM9GaM28YdaSC935jtYMKYCIEVox5r2aVFaMQwaUTNPqkPIU09zyfaEhFLy8oVUVN7JFYntq45adujIFtbjoUXilJXj2NkR6x7AHJtseLSopymsv_XsinY7HnerdT28r_Uh9b1bDsoBynXklWnioEd5qC3E4OBRPBl7-MYA0H1xtRULsrd_CWl8St64DgIMYIu9rV4_jefgXBithVYyiNmt7ryHu4SY',
            'nickname': 'true'
        }
    req = requests.post(url=url, headers=login_headers, data=data, verify=False, cookies=cookie)
    temp = dict_from_cookiejar(req.cookies)
    if temp:
        with open('./cookie.txt', 'wb') as f:
            pickle.dump(temp, f)


def get_cookie():
    try:
        with open('./cookie.txt', 'rb') as f:
            cookie = pickle.load(f)
        if not cookie:
            return {}
        return cookie
    except:
        return {}


def get_hot_actor():
    url = PREFIX + "actor/HotStarPartial/1/100"
    cookie = get_cookie()
    req = requests.get(url=url, headers=headers, cookies=cookie, verify=False)
    req.encoding = 'utf-8'
    print(req.text)
    try:
        result = json.loads(req.text)
    except Exception as e:
        login()
        return req.text
        print(e)
    hot_list = result['partialViewListModel']['result']
    for hot in hot_list:
        hot['actor_name'] = hot['actorName']
        hot['online_photo'] = hot['onLinePhoto']
        hot['new_movie_name'] = hot['newMovie']
        del hot['actorName']
        del hot['onLinePhoto']
        del hot['newMovie']
        star = Star(**hot)
        star.save()


def get_movie_by_actor():
    url = PREFIX + 'movie/ActorFilterNew/1/100/1/0/1/0/0'
    cookie = get_cookie()
    star_id_list = Star.objects.all().values('id')
    for star_id in star_id_list:
        id = star_id['id']
        movies = Movie.objects.filter(star__id=id)
        if len(movies) > 0:
            continue
        time.sleep(10)
        params = {
            'id': id,
            'movieType': '-1',
            'canLoad': '0',
            'hadWatch': '0',
            'signalPlay': 'false'
        }
        req = requests.get(url=url, params=params, headers=headers, cookies=cookie, verify=False)
        req.encoding = 'utf-8'
        print(req.text)
        try:
            result = json.loads(req.text)['result']
            for movie in result:
                movie['can_load'] = movie['canLoad']
                movie['can_online'] = movie['canOnLine']
                movie['fan_num'] = movie['fanNum']
                movie['movie_type'] = movie['movieType']
                movie['new_cloud_time'] = movie['newCloudTime']
                movie['push_time'] = movie['pushTime']
                del movie['canLoad']
                del movie['canOnLine']
                del movie['fanNum']
                del movie['movieType']
                del movie['newCloudTime']
                del movie['pushTime']
                del movie['todayNewMovie']
                del movie['hadCommOrWatch']
                movie['labels'] = ",".join(movie['lables'])
                del movie['lables']
                movie_model = Movie(**movie)
                movie_model.save()
                obj = Movie.objects.get(id=movie['id'])
                obj.star.add(id)
        except Exception as e:
            print(e)
            login()
            break


def get_desc():
    movie_list = Movie.objects.all()
    cookie = get_cookie()
    try:
        for movie in movie_list:
            url = PREFIX + 'movie/DetailDes/'
            if movie.describe:
                continue
            time.sleep(10)
            url += movie.id
            req = requests.get(url=url, headers=headers, cookies=cookie, verify=False)
            res = json.loads(req.text)['data']
            movie.describe = res['showDescribe']
            movie.save()
    except Exception as e:
        print(e)
        login()


def get_photo_method():
    movie_list = Movie.objects.all()
    cookie = get_cookie()
    try:
        for movie in movie_list:
            url = PREFIX + 'photo/PartialFilter/3/%s/1/36' % (movie.id)
            videos = Photo.objects.filter(video=movie)
            if len(videos) > 0:
                continue
            time.sleep(10)
            req = requests.get(url=url, headers=headers, cookies=cookie, verify=False)
            result = json.loads(req.text)
            paths = result['result']
            for path in paths:
                Photo.objects.create(id=uuid.uuid4(), video=movie, path=path)
    except Exception as e:
        print(e)
        login()


def get_video_path(video_id):
    url = 'https://m.pearkin.com/api/moviePlay/GetMovieCloud/%s' % (video_id)
    video_headers = {
        'Host': 'm.pearkin.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; FIG-AL10 Build/HUAWEIFIG-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'X-Requested-With': 'com.pear.hot',
        'Referer': 'https://m.pearkin.com/movie/movieDetail'
    }
    data = {
        'onlyCzn': '1'
    }
    cookie = get_cookie()
    req = requests.get(url=url, headers=video_headers, params=data, cookies=cookie, verify=False)
    result = json.loads(req.text)
    ret = {
        'full_path_url': '',
        'thumbnail': '',
    }
    ret['thumbnail'] = result['thumbnail']
    if len(result['resolution']):
        url = result['resolution'][0]['url']
        ret['full_path_url'] = url
        # # cmd = 'vlc.exe  -vvv "%s"  :sout=#transcode{vcodec=theo,vb=800,acodec=vorb,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=ogg,dst=:8080/%s} :no-sout-all :sout-keep' % (
        #     url, video_id)
        # subprocess.Popen(cmd, shell=True)
        return ret
    else:
        data = {
            'onlyCzn': '0'
        }
        req = requests.get(url=url, headers=video_headers, params=data, cookies=cookie, verify=False)
        result = json.loads(req.text)
        if len(result['resolution']):
            url = result['resolution'][0]['url']
            ret['full_path_url'] = url
            # cmd = 'vlc.exe  -vvv "%s"  :sout=#transcode{vcodec=theo,vb=800,acodec=vorb,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=ogg,dst=:8080/%s} :no-sout-all :sout-keep' % (
            #     url, video_id)
            # subprocess.Popen(cmd, shell=True)
        return ret


def get_community():
    i = 1
    cookie = get_cookie()
    try:
        while True:
            url = PREFIX + 'photoFindMovie/IndexNew/%d/15' % (i)
            i += 1
            req = requests.get(url=url, headers=headers, cookies=cookie, verify=False)
            time.sleep(10)
            result = json.loads(req.text)
            models = result['model']
            for model in models:
                source, Flag = Source.objects.get_or_create(id=model['id'])
                source.text = model['photoText']
                source.fan_num = model['fanNum']
                source.content = model['contents']
                source.local_path = model['localPath']
                source.save()
    except Exception as e:
        print(e)
        login()
