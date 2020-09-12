from django.contrib import admin

from .models import SlideShowBottom,SlideShowTop
# Register your models here.

@admin.register(SlideShowTop)
class SlideShowTopAdmin(admin.ModelAdmin):
    pass


@admin.register(SlideShowBottom)
class SlideShowBottomAdmin(admin.ModelAdmin):
    pass