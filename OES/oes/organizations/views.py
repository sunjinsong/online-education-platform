from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher,Organization,OrganizationCategory,City
# Create your views here.
from courses.models import Course
from django.core.paginator import Paginator
def TeacherList(request):
    page = request.GET.get('page',1)
    try:
        page = int(page)
    except:
        return HttpResponse('页码错误')
    teacher_list = Teacher.objects.all()
    p = Paginator(teacher_list,1)
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

    teacher_list = p.page(page).object_list
    hotteacher_list = Teacher.objects.all().order_by('learn_num')[:5]
    context={
        'teacher_list':teacher_list,
        'flag': 'teacher',
        'hotteacher_list':hotteacher_list,

        'next': nextpage,
        'last': last,
        'page_list': page_list,
        'page': page,
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
    city = request.GET.get('city',False)
    ct = request.GET.get('ct',False)
    sort = request.GET.get('sort',False)
    if not any([city,ct,sort]):       #表示没有指定  查询全部
        organization_list = Organization.objects.all()
    elif city:                  #表示指定city
        organization_list = Organization.objects.filter(city=city)
    elif ct:
        #得到类别
        type_org=OrganizationCategory.objects.filter(id=ct)[0]
        organization_list = Organization.objects.filter(organizationcategory=type_org)
    else:
        organization_list = Organization.objects.all().order_by(sort)


    page = request.GET.get('page',1)
    try:
        page = int(page)
    except:
        return HttpResponse('页码错误')
    teacher_list = Teacher.objects.all()
    p = Paginator(teacher_list,1)
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

    organization_list = p.page(page).object_list
    #根据机构的学习数来排名
    hotorganization_list = Organization.objects.all().order_by('learn_num')[:3]
    typelist = OrganizationCategory.objects.all()
    citylist = City.objects.all()
    context={
        'organization_list':organization_list,
        'typelist':typelist,
        'citylist':citylist,
        'flag': 'organization',
        'hotorg_list':hotorganization_list,

        'next': nextpage,
        'last': last,
        'page_list': page_list,
        'page': page,
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
        'org_id': org_id,
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




def OrganizationDetailDes(request,org_id):
    orgs = Organization.objects.filter(id=org_id)
    if not orgs:
        return HttpResponse('机构不存在')

    org=orgs[0]
    context={
        'org_id':org_id,
        'introduce':org.introduce,
    }
    return render(request,'organization/org-detail-desc.html',context=context)


def OrganizationDetailTeacher(request,org_id):
    orgs = Organization.objects.filter(id=org_id)
    if not orgs:
        return HttpResponse('机构不存在')
    org = orgs[0]
    teacher_list = Teacher.objects.filter(organization=org)
    context={
        'org_id':org_id,
        'teacher_list':teacher_list,
    }
    return render(request,'organization/org-detail-teachers.html',context=context)