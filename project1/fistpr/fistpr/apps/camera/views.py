from django.shortcuts import render
from .models import info,comment

def index(request):

    list_info=info.objects.all()
    return render(request,'camera/list.html',{'list_info':list_info})


# Create your views here.
