from django.contrib import admin

import Monitor.models
# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_addr', 'status')

admin.site.register(Monitor.models.Host,HostAdmin)
admin.site.register(Monitor.models.HostGroup)
admin.site.register(Monitor.models.Template)
admin.site.register(Monitor.models.Service)
admin.site.register(Monitor.models.Trigger)
admin.site.register(Monitor.models.ServiceIndex)
admin.site.register(Monitor.models.Action)
admin.site.register(Monitor.models.ActionOperation)
admin.site.register(Monitor.models.Maintenance)
