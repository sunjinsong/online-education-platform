from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher,Organization,OrganizationCategory,City
# Create your views here.
from courses.models import Course
def TeacherList(request):
    teacher_list = Teacher.objects.all()[:5]
    context={
        'teacher_list':teacher_list,
    }
    return render(request,'organization/teachers-list.html',context=context)


def TeacherDetail(request,teacher_id):
    teacher=Teacher.objects.filter(id=teacher_id)
    if not teacher:
        return HttpResponse('不存在这个老师')
    teacher=teacher[0]
    course_list = Course.objects.filter(teacher=teacher)
    context={
        'teacher':teacher,
        'course_list':course_list,
    }

    return render(request,'organization/teacher-detail.html',context=context)


def OrganizationList(request):
    organization_list = Organization.objects.all()[:5]
    typelist = OrganizationCategory.objects.all()
    citylist = City.objects.all()
    context={
        'organization_list':organization_list,
        'typelist':typelist,
        'citylist':citylist,
    }
    return render(request,'organization/org-list.html',context=context)


def OrganizationDetailCourse(request,org_id):
    org = Organization.objects.filter(id=org_id)
    if not org:
        return HttpResponse('不存在机构')
    teachers = Teacher.objects.filter(organization=org_id)        #得到一个机构的所有的老师
    course_list=[]
    for teacher in teachers:
        courses=Course.objects.filter(teacher=teacher)
        course_list.extend(courses)
    context={
        'course_list':course_list,
    }
    return render(request,'organization/org-detail-course.html',context=context)



def OrganizationDetailPagehome(request,org_id):
    org = Organization.objects.filter(id=org_id)
    if not org:
        return HttpResponse('不存在机构')
    org=org[0]
    teachers = Teacher.objects.filter(organization=org_id)        #得到一个机构的所有的老师
    course_list=[]
    for teacher in teachers:
        courses=Course.objects.filter(teacher=teacher)
        course_list.extend(courses)
    context={
        'course_list':course_list[:4],
        'teachers':teachers[:3],
        'org':org,
        'org_id':org_id,
    }
    return render(request,'organization/org-detail-homepage.html',context=context)