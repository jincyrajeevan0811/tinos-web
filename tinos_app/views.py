from django.shortcuts import render

def index (request):
    return render(request, 'index.html')


def service(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')