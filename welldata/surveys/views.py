from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Survey


def index(request):
    surveys = Survey.objects.all()
    return render(request, 'surveys/index.html', {'surveys': surveys})


def detail(request, survey_id):
    surveys = get_object_or_404(Survey, id=survey_id)
    return render(request, 'surveys/detail.html', {'surveys': surveys})
