from django.contrib import admin

from .models import Course,Chapter,Video,resource
# Register your models here.
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(resource)
class resourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass