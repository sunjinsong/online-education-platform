from django.urls import path
from . import views
urlpatterns=[
    path('teacherlist/',views.TeacherList,name='teacherlist'),
    path('teacherdetail/<int:teacher_id>',views.TeacherDetail,name='teacherdetail'),
    path('organizationlist/',views.OrganizationList,name='organizationlist'),
    path('organizationdetailcourse/<int:org_id>',views.OrganizationDetailCourse,name='organizationdetailcourse'),
    path('organizationdetailpagehome/<int:org_id>', views.OrganizationDetailPagehome, name='organizationdetailpagehome'),
    path('organizationdetaildesc/<int:org_id>', views.OrganizationDetailDes, name='organizationdetaildesc'),
    path('organizationdetailteacher/<int:org_id>', views.OrganizationDetailTeacher, name='organizationdetailteacher'),
]