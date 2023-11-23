from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#should access model objects and use Templates to prepare response

    return HttpResponse('Hello World')

# Create your views here.
