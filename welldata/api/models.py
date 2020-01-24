from django.db import models
from tastypie.resources import ModelResource
from surveys.models import Survey


class SurveyResource(ModelResource):
    class Meta:
        queryset = Survey.objects.all()
        resource_name = 'surveys'
