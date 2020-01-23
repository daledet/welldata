from django.http import HttpResponse
from django.shortcuts import render
from .models import Survey
# Create your views here.


def index(request):
    surveys = Survey.objects.all()
    output = ', '.join([s.survey for s in surveys])
    return HttpResponse(output)
