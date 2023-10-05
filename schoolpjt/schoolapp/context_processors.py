from .models import Category
from .models import Course
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)
def sub_links(request):
    slinks=Course.objects.all()
    return dict(clinks=slinks)