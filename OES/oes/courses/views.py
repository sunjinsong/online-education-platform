from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Course
from organizations.models import Teacher
def CourseList(request):
    course_list = Course.objects.all()[:9]
    context={
        'course_list':course_list,
    }
    return render(request,'course/course-list.html',context=context)



def CourseDetail(request,course_id):
    course = Course.objects.filter(id = course_id)
    if not course:
        return HttpResponse('没有这个课程')

    course = course[0]

    context={
        'course':course,
    }

    return render(request,'course/course-detail.html',context=context)


def CourseChapter(request,course_id):
    course = Course.objects.filter(id=course_id)
    if not course:
        return HttpResponse('没有这个课程')

    course = course[0]

    context = {
        'course': course,
    }

    return render(request, 'course/course-video.html', context=context)


