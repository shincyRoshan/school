from.import views
from django.urls import path
from django.urls import path, include



app_name='schoolapp'
urlpatterns = [

    path('', views.index, name='index'),
    path('/category', views.AllProdCat, name='AllProdCat'),
    path('location', views.location, name='location'),
    path('add_personal_details', views.add_personal_details, name='add_personal_details'),

]
