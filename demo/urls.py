from django.conf.urls import patterns, url

from demo import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

)

# EOF