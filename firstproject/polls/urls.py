from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('polls/', views.index, name='index'),
    path('polls/tags', views.tags, name='tags'),
    path('demo/', views.home_view, name='home'),#filterd tags

    path('details/',views.poll_details,name='index'),
    path('pollvotes/',views.pollvotes,name='index'),

    path('upvotes/', views.update_votes, name='index'),
    # ex: /polls/
    path('add/',views.add,name='add'),
    path('createpost/', views.createpost, name='createpost'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]