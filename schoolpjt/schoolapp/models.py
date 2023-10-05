from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    link=models.CharField(max_length=250,blank=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('schoolapp:products_by_category',args=[self.slug])



    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
class Person(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


