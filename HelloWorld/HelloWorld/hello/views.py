from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#should access model objects and use Templates to prepare response
    text = "Hello World!"
    return render(request, 'index.html', {'text': text})
