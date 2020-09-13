from django.urls import path
from . import views
from haystack.views import SearchView
urlpatterns=[
    path('courselist/',views.CourseList,name='courselist'),
    path('coursedetail/<int:course_id>/',views.CourseDetail,name='coursedetail'),
    path('coursechapter/<int:course_id>/',views.CourseChapter,name='coursechapter'),
    path('video/<int:video_id>/',views.VideoOpen,name='video'),
    # path('search/', SearchView(), name='haystack_search'),

]