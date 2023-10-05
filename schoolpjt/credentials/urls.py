from.import views
from django.urls import path, include

urlpatterns = [


    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    # path('detail', views.detail, name='detail'),
    path('logout', views.logout, name='logout'),
]
