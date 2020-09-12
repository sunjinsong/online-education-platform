from django.contrib import admin

from .models import Course,Chapter,Video,resource
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass