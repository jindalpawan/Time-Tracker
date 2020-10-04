from django.contrib import admin
from .models import Project, Timing

# provide access to admin of Timing and Project models.
admin.site.register(Timing)
admin.site.register(Project)
