from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Artical
import markdown

# Create your views here.

def index(request):
    artical_list = Artical.objects.all().order_by('-create_time')
    return render(request, 'flyingzone/index.html', context={
        'artical_list': artical_list
    })

def detail(request, pk):
    artical = get_object_or_404(Artical, pk=pk)
    artical.content = markdown.markdown(artical.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'flyingzone/detail.html', context={'artical': artical})
    