from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('WellSav Chat')


def about(request):
    return HttpResponse('WellSav About')
