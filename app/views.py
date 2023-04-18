from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='r')
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(name__in=('raina','ashok'))
    LOW=Webpage.objects.filter(name__contains='o')
    LOW=Webpage.objects.filter(name__regex='[a-z A-Z]{2}')
    LOW=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='MSD'))
    LOW=Webpage.objects.filter(Q(topic_name='cricket') | Q(topic_name='boxing'))
    LOW=Webpage.objects.filter(name='ashok').delete()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',d)














def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2022-01-12')
    LOA=AccessRecord.objects.filter(date__lt='2022-01-12')
    LOA=AccessRecord.objects.filter(date__gte='2021-04-14')
    LOA=AccessRecord.objects.filter(date__lte='2021-04-14')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__year='2022')
    LOA=AccessRecord.objects.filter(date__month='04')
    LOA=AccessRecord.objects.filter(date__day='16')
    d={'access':LOA}
    return render(request,'display_access.html',d)