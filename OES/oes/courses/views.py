from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.paginator import Paginator

from .models import Course,Chapter,resource,Video
from organizations.models import Teacher,Organization
def CourseList(request):
    page = request.GET.get('page',1)
    try:
        page = int(page)
    except:
        return HttpResponse('页码错误')
    course_list = Course.objects.all()
    p = Paginator(course_list,1)
    if p.num_pages<page:
        page = p.num_pages
    if page < 1:
        page = 1

    nextpage = 0
    last = 0
    if page-2 >0 and page+2 <= p.num_pages:
        nextpage = page+1
        last = page-1
        page_list = [page-2,page-1,page,page+1,page+2]
        print(page_list)
    elif page-2 <= 0 and page+2 >= p.num_pages:
        page_list = [x for x in range(1,p.num_pages+1)]
    elif page-2 <= 0 and page+ 2 < p.num_pages:
        page_list = [x for x in range(1,page+3)]
        nextpage = page+1
    else:
        page_list = [x for x in range(page-2,p.num_pages+1)]
        last = page-1
    hotcourse_list = Course.objects.all().order_by('fav_num')

    course_list = p.page(page).object_list
    context={
        'course_list':course_list,
        'flag': 'course',
        'hotcourse_list':hotcourse_list[:3],

        'next':nextpage,
        'last':last,
        'page_list':page_list,
        'page':page,
    }
    return render(request,'course/course-list.html',context=context)



def CourseDetail(request,course_id):
    course = Course.objects.filter(id = course_id)
    if not course:
        return HttpResponse('没有这个课程')

    course = course[0]
    org = course.teacher.organization
    context={
        'course':course,
        'org':org,
    }

    return render(request,'course/course-detail.html',context=context)


def CourseChapter(request,course_id):
    course = Course.objects.filter(id=course_id)
    course = course[0]
    if not course:
        return HttpResponse('没有这个课程')
    source_list = resource.objects.filter(course=course)
    teacher = course.teacher
    chapter_list = Chapter.objects.filter(course=course)

    for chapter in chapter_list:
        video_list = Video.objects.filter(chapter=chapter)
        chapter.video_list = video_list

    context = {
        'course': course,
        'source_list':source_list,
        'chapter_list':chapter_list,
        'teacher':teacher,
    }

    return render(request, 'course/course-video.html', context=context)


def VideoOpen(request,video_id):
    video = Video.objects.filter(id=video_id)
    if not video:
        return HttpResponse('视频已经不存在')

    context={
        'url':video[0].url,
    }

    return render(request,'course/video.html',context=context)
