from tmproject import settings
from . import views

from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [

    path('',views.demo,name='demo'),



]

