from django.shortcuts import render
from .models import SlideShowTop,SlideShowBottom
# Create your views here.
from courses.models import Course
from organizations.models import Organization

def index(request):
    slides=SlideShowTop.objects.all()
    slides_bottom = SlideShowBottom.objects.all()
    course_list = Course.objects.all()[:6]
    org_list = Organization.objects.all()[:15]
    context={
        'slides':slides,
        'slides_bottom':slides_bottom,
        'course_list':course_list,
        'org_list':org_list,
        'flag':'index',
    }
    return render(request,'index.html',context=context)