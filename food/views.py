from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint


def index(request):
    return render(request, 'food/index.html', context=None)


def random_number(request):
    num = randint(0, 100)
    return HttpResponse(f'wylosowano liczbe:{num}')

def random_number_max(request,max):
    num = randint(0, max)
    return HttpResponse(f' Uzytkownik podal wartosc {max}. Wylosowano liczbe:{num}')



def random_number_mixed(request,min_, max_):
    num = randint(min_, max_)
    return HttpResponse(f' Uzytkownik podal wartosci minimum  {min_} oraz maksimum {max_}. Wylosowano liczbe:{num}')

def hello(request, name):
    return HttpResponse(f'hello {name}!')

