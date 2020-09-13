from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def AddFav(request):
    add_type = request.GET['fav_type']
    add_id = request.GET['fav_id']
    print(add_type,add_id)
    return JsonResponse({'status':'success','msg':'收藏成功'})
