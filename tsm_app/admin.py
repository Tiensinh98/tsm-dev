from django.contrib import admin
from . import app_tools

admin.site.register(app_tools.CustomUser)
admin.site.register(app_tools.Staff)
admin.site.register(app_tools.Profile)
admin.site.register(app_tools.Telephone)
admin.site.register(app_tools.Project)
admin.site.register(app_tools.Task)
admin.site.register(app_tools.Team)
admin.site.register(app_tools.Device)
