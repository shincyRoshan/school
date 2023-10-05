from django.contrib import admin
from . models import  Category
from . models import  Course
from . models import  Person
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Person)