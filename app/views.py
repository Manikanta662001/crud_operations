from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)
def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    #LOW=Webpage.objects.get(topic_name='boxing')
    LOW=Webpage.objects.exclude(topic_name='cricket')
    LOW=Webpage.objects.all()[1:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('topic_name'))
    LOW=Webpage.objects.all().order_by(Length('topic_name').desc())
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)
def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-01-12')
    LOA=AccessRecord.objects.filter(date__lt='2022-01-12')
    LOA=AccessRecord.objects.filter(date__gte='2021-04-14')
    LOA=AccessRecord.objects.filter(date__lte='2021-04-14')
    d={'access':LOA}
    return render(request,'display_access.html',d)