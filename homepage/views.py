from django.shortcuts import render, get_object_or_404

from .models import Introduction, NewsItem, Link


# Create your views here.
def index(request):
    args = {}
    return render(request, 'home/index.html',
        {
        'introductions': Introduction.objects.all(),
        'news': NewsItem.objects.all().order_by('-posted', 'title')[:5],
        'links': Link.objects.all(),
        }
    )
