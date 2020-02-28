from django.contrib import admin

# Register your models here.
from .models import Group, Todo

class GroupAdmin(admin.ModelAdmin):
    list_display = ("id","name")

class TodoAdmin(admin.ModelAdmin):
    list_display = ("uuid","content","created_at","updated_at","pub_user","pub_group","column","importance_level")

admin.site.register(Group, GroupAdmin)
admin.site.register(Todo, TodoAdmin)