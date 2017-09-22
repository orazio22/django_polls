from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/detail1/$', views.DetailView1.as_view(), name='detail1'),
    url(r'^(?P<pk>[0-9]+)/detail2/$', views.DetailView2.as_view(), name='detail2'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/vote1/$', views.vote1, name='vote1'),
    url(r'^(?P<question_id>[0-9]+)/vote2/$', views.vote2, name='vote2'),
    url(r'^saveIP/$', views.saveIP, name='saveIP'),
    url(r'^IP-adresse/$', views.IpView.as_view(), name='ip'),
]
