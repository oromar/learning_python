from django.contrib import admin
from core.models import Event

class AdminEvent(admin.ModelAdmin):
    list_display= ('title', 'event_date', 'creation_date')
    list_filter = ('title', 'description', 'user')

# Register your models here.
admin.site.register(Event, AdminEvent)