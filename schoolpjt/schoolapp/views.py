from ctypes import c_int
from itertools import combinations
from pydoc_data.topics import topics

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.templatetags.rest_framework import data

from .models import Category
from .models import Course
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage



from django.shortcuts import render




from .models import Course

from django.shortcuts import render

from .models import Course
from .forms import LocationForm

def location(request):
    form = LocationForm()
    return render(request, 'drop.html', {'form': form})

def index(request):

    return render(request, "index.html")
def AllProdCat(request,c_slug=None):
    c_page=None
    Product_List=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        COURSE_lIST=Course.objects.all().filter(category=c_page ,available=True)
    else:
        COURSE_lIST = Course.objects.all().filter(available=True)
    paginator=Paginator(Product_List,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'credentials/detail.html',{'category':c_page,'course':products})




from django.shortcuts import render, redirect


# def add_personal_details(request):
#     task = Perdonala.objects.all()
#     if request .method=="POST":
#
#         category_id = request.POST.get("category",'')  # Assuming this is the value from the dependent dropdown
#
#         # Retrieve the Category instance based on the category_id
#         # category = Category.objects.get(id=category_id)
#
#         course_id = request.POST.get("course") # Replace with the actual ID value
#         # course = Course.objects.get(id=course_id)
#
#
#
#
#
#         name=request.POST.get('name',''),
#         dob=request.POST.get('date',''),
#         age=request.POST.get('age',''),
#         gender=request.POST.get('gender',''),
#         phone=request.POST.get('phone',''),
#         email=request.POST.get('email',''),
#
#
#         prsn=Perdonala(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,category=category_id,course=course_id)
#         prsn.save()
#
#     return render(request, 'drop.html', {'tasks': task})

from .models import Person
from django.contrib.auth.models import User
from django.contrib import messages, auth
def add_personal_details(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('date')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address=request.POST.get('address')
        category_id = request.POST.get('category')
        course_id = request.POST.get('course')
        uid=request.POST.get('uid')

        # Create and save the Perdonala object
        perdonala = Person(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            category_id=category_id,
            course_id=course_id,
            user_id=uid
        )
        perdonala.save()

        # Redirect to a success page or any other desired page
        task = Person.objects.all()
    return render(request, 'drop.html',{'tasks': task})

    # Render the initial form page if it's a GET request
    # return render(request, 'perdonala_form.html')