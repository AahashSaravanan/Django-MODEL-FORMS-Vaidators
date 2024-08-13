from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_student(request):
    d={'ESMF':StudentMF()}
    if request.method=='POST':
        SMFO = StudentMF(request.POST)
        if SMFO.is_valid():
            SMFO.save()
            return HttpResponse('Data is inserted')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_student.html',d)