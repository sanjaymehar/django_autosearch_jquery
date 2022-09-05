from pickletools import read_uint1
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def name(request):
    search=request.GET.get('term')   #fetching from id in html #terms is inbuild object of seacrch api
    names=[]
    if search:
        names_obj=Name.objects.filter(name__startswith=search)         #we can also use __icontains
        for i in names_obj:
            names.append(i.name)
    
    return JsonResponse(names,safe=False)
    

def home(request):
    return render(request,"home.html")