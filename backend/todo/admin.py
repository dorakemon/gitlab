from django.contrib import admin

# Register your models here.
from .models import Group, Column, Todo

class GroupAdmin(admin.ModelAdmin):
    list_display = ("uuid","name")

class TodoAdmin(admin.ModelAdmin):
    list_display = ("uuid","content","created_at","updated_at","pub_user","pub_group","column","importance_level","deadline")

admin.site.register(Group, GroupAdmin)
admin.site.register(Column)
admin.site.register(Todo, TodoAdmin)