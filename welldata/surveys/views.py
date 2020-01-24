from django.http import HttpResponse
from django.shortcuts import render
from .models import Survey


def index(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys/index.html', {'surveys': surveys})
