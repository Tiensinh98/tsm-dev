from django.contrib import admin
from . import models


admin.site.register(models.Worker)
admin.site.register(models.Leader)
admin.site.register(models.WorkerTelephone)
admin.site.register(models.Project)
admin.site.register(models.Task)
