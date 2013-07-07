from django.contrib import admin
from app.models import Profile, Event
 
class ProfileAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['description']
    # fields to filter the change list with
    list_filter = ['active', 'created']
    # fields to search in change list
    search_fields = ['description', 'interests']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
 
admin.site.register(Profile, ProfileAdmin)

class EventAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description']
    # fields to filter the change list with
    list_filter = ['when']
    # fields to search in change list
    search_fields = ['title', 'description', 'interests']
    # enable the date drill down on change list
    date_hierarchy = 'when'
    # enable the save buttons on top on change form
    save_on_top = True
 
admin.site.register(Event, EventAdmin)
