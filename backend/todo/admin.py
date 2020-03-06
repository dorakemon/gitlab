from django.contrib import admin

# Register your models here.
from .models import Group, Column, Todo

class GroupAdmin(admin.ModelAdmin):
    list_display = ("uuid","name","_column","_user_in_group")
    def _column(self, row):
        return ',  '.join([x.name for x in row.column.all()])
    def _user_in_group(self,row):
        return ',  '.join([x.username for x in row.user_in_group.all()])

class ColumnAdmin(admin.ModelAdmin):
    # list_display = ("name")
    list_display = ["name"]

class TodoAdmin(admin.ModelAdmin):
    list_display = ("uuid","content","created_at","updated_at","pub_user","pub_group","column","importance_level","deadline")

admin.site.register(Group, GroupAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Todo, TodoAdmin)