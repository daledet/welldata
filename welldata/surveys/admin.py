from django.contrib import admin
from .models import Well, Survey


class WellAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('survey', 'measured_depth', 'inclination', 'azimuth')


admin.site.register(Well, WellAdmin)
admin.site.register(Survey, SurveyAdmin)
