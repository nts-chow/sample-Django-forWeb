from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse('hello Django!!!')
    context = {'title': 'Templates context test'}
    return render(request, 'Book/index.html', context)
