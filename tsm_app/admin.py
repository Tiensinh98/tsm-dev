from django.contrib import admin
from . import app_tools

admin.site.register(app_tools.Worker)
admin.site.register(app_tools.Leader)
admin.site.register(app_tools.WorkerTelephone)
admin.site.register(app_tools.Project)
admin.site.register(app_tools.Task)
admin.site.register(app_tools.Device)
admin.site.register(app_tools.DeviceUserHistory)
admin.site.register(app_tools.CustomUser)
