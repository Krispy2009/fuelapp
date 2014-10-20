from django.conf.urls import patterns,url

import views

urlpatterns = patterns('',
        url(r'^$',views.index, name='index'),
        url(r'^aboutus',views.aboutus, name='aboutus'),
        url(r'^add_station', views.add_station, name='add_station'),
        url(r'^station/(?P<station_name_slug>[\w\-]+)/$',views.station,name='station')
        )
