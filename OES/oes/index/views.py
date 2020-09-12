from django.shortcuts import render
from .models import SlideShowTop,SlideShowBottom
# Create your views here.


def index(request):
    slides=SlideShowTop.objects.all()
    context={
        'slides':slides,
    }
    return render(request,'index.html',context=context)