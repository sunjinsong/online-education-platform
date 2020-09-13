from django.urls import path
from . import views

urlpatterns=[
    path('add_fav/',views.AddFav,name='add_fav'),
]