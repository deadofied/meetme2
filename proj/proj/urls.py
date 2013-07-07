from django.conf.urls import patterns, include, url
from django.contrib import admin
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index'),
    url(r'^newsfeed/', 'app.views.newsfeed'),
    url(r'^home/', 'app.views.home'), 
    url(r'^edit/', 'app.views.edit'),                       
    url(r'^register/', 'app.views.register'),  
    url(r'^authorize/', 'app.views.authorize'), 
    url(r'^loginview/', 'app.views.loginview'), 
    url(r'^deauthorize/', 'app.views.deauthorize'),   
    url(r'^aboutus/', 'app.views.aboutus'),  
    url(r'^newevent/', 'app.views.newevent'),  
    url(r'^(?P<slug>[\w\-]+)/$', 'app.views.profile'),
)
