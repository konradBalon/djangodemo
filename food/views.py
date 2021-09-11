from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint


def index(request):
    return render(request, 'food/index.html', context=None)


def random_number(request):
    num = randint(0, 100)
    return HttpResponse(f'wylosowano liczbe:{num}')
