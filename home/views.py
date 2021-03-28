from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'home'}
    return render(request, 'index.html', context)

def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'aboutus'}
    # the reason why we used 'page' is we can use a if operation if we need
    return render(request, 'aboutus.html', context)

def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'references'}
    # the reason why we used 'page' is we can use a if operation if we need
    return render(request, 'references.html', context)

def contact(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'contact'}
    # the reason why we used 'page' is we can use a if operation if we need
    return render(request, 'contact.html', context)
