from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import University, Faculty, Course, Place, User

from django.contrib.auth.admin import UserAdmin


from django.utils.translation import gettext, gettext_lazy as _

class FacultyAdmin(admin.ModelAdmin):
    list_display = ("university", "name")
    ordering = ["-university", "id"]

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "season_name", "department_name")
    ordering = ["name", "id"]


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password', 'gender', 'birthday', 'university_faculty', 'place')}),
        (_('Personal info'), {'fields': ('email', 'course')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_staff', 'gender', 'birthday', 'university_faculty', 'place', '_course')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')#, 'university_faculty', 'place')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions', 'course')

    def _course(self, row):
        return ',  '.join(["{}{}{}".format(x.name, x.season_name, x.department_name) for x in row.course.all()])


admin.site.register(University)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Place)

admin.site.register(User, CustomUserAdmin)