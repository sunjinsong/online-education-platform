from django.urls import path
from . import views
urlpatterns=[
    path('courselist/',views.CourseList,name='courselist'),
    path('coursedetail/<int:course_id>/',views.CourseDetail,name='coursedetail'),
    path('coursechapter/<int:course_id>/',views.CourseChapter,name='coursechapter'),

]