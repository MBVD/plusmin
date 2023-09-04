from codecs import utf_7_decode
from datetime import datetime
from django import template
from Fsite.models import *
from Fsite.forms import *


def get_time(request):
    return {"time": datetime.now()}

def urls_for_mobile(request):
    url = "/login/"
    if request.user.is_authenticated:
        url = "/user/" + request.user.username
    return {"urls_for_mobile": {"Главная": "/", "Личный кабинет": url, "Рейтинг": "/rating/", "Материалы": "/problems/", "Соревнования": "/contests/", "Статьи": "/news/", "О сайте": "/about/", "Поиск": "/find_information"}}

def get_navigation_pannel(request):
    return {"navigation_pannel": {"Главная": "/", "Рейтинг": "/rating/", "Материалы": "/problems/", "Соревнования": "/contests/", "Статьи": "/news/", "О сайте": "/about/"}}