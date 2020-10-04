from django.contrib import admin
from .models import Project, Timing
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
	fields= ['name']

# class TimingAdmin(admin.ModelAdmin):
# 	fields= ['task', 'projects', 'user', 'start', 'end']


admin.site.register(Timing)
admin.site.register(Project, ProjectAdmin)