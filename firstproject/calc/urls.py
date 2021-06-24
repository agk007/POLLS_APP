from django.urls import path

from . import views



urlpatterns = [

    path('about/',views.about,name='index'),
    path('index/',views.index,name='index'),

    # ex: /polls/5/

]