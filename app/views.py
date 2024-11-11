from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def studentfrm(request):
    ESFO=StudentForms()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')





    return render(request,'studentfrm.html',d)