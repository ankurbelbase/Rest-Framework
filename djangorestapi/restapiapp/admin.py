from django.contrib import admin

# Register your models here.
from restapiapp.models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ['name','loaction','date']

admin.site.register(Event)